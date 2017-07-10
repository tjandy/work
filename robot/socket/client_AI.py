import static
import msg_pb2
from  gameEvent import MyEvent
from packetid import PacketID

Numbers = static.enum( INIT=1, WAIT_LOGIN = 2,LOGIN_SUCCESS=3, WAIT_MATCH=4,MATCH_SUCCESS=5,WAIT_READY=6,
                       READY_SUCCESS=7,ENTERROOM=8,CLOSE=9 )

class AI_Control(object):
    def __init__(self,netClient):
        self.client = netClient
        self.state = Numbers.INIT
        self.enable = False
        self._regiestEvent(netClient.dispatcher)

    def _regiestEvent(self,event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.event_dispatcher.add_event_listener(MyEvent.SET_USER_ID, self.event_setUserId)
        self.event_dispatcher.add_event_listener(MyEvent.QUEUE_UPDATE, self.event_queueUpdate)

    def startTick(self):
        self.enable = True

    def setNick(self,nick):
        self.Nick = nick

    def setDeviceId(self,id):
        self.deviceId = id


    def event_setUserId(self,event):
        self.userId = event.data
        self.state = Numbers.LOGIN_SUCCESS

    def event_queueUpdate(self,event):
        num  = event.data
        print("event_queueUpdate user nick"+ self.Nick)
        print("event_queueUpdate user readynum" + str(num))
        if num <= 1 :
            self.state = Numbers.MATCH_SUCCESS
        elif num == static.ROOM_NUM :
            self.state = Numbers.READY_SUCCESS

    def tick(self):
        if self.enable == False:
            return
        if self.state ==  Numbers.INIT:
            self.sendLogin()
        elif self.state == Numbers.LOGIN_SUCCESS:
            self.sendStartMatching()
        elif self.state == Numbers.MATCH_SUCCESS:
            self.sendReady()
        elif self.state == Numbers.READY_SUCCESS:
            self.sendLoading()

    def sendLogin(self):
        msg = msg_pb2.cs_loginGame()
        msg.deviceid = self.deviceId
        msg.nick = self.Nick
        self.client.sendMsg(PacketID.cs_loginGame, msg.SerializeToString())
        self.state = Numbers.WAIT_LOGIN

    def sendStartMatching(self):
        msg = msg_pb2.cs_startMatching()
        msg.type  = static.ROMM_TYPE
        self.client.sendMsg(PacketID.cs_startMatching, msg.SerializeToString())
        self.state = Numbers.WAIT_MATCH

    def sendReady(self):
        msg = msg_pb2.cs_ready()
        msg.userid = self.userId
        self.client.sendMsg(PacketID.cs_ready, msg.SerializeToString())
        self.state = Numbers.WAIT_READY
        print("send ready nick:"+self.Nick)

    def sendLoading(self):
        msg = msg_pb2.cs_loading()
        msg.progress = 100;
        self.client.sendMsg(PacketID.cs_loading, msg.SerializeToString())
        self.state = Numbers.ENTERROOM
        print("sendLoading nick:" + self.Nick)

