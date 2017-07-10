import msg_pb2
from gameEvent import MyEvent
from packetid import PacketID

class packetHandler(object):
    def __init__(self,event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.event_dispatcher.add_event_listener(PacketID.sc_loginGame, self.on_packet_login)
        self.event_dispatcher.add_event_listener(PacketID.sc_startMatching, self.on_packet_startMatching)
        self.event_dispatcher.add_event_listener(PacketID.br_queueStatus, self.on_packet_queueStatus)

    def on_packet_login(self,event):
        scMsg = msg_pb2.sc_loginGame()
        scMsg.ParseFromString(event.data)
        self.event_dispatcher.dispatch_event(MyEvent(MyEvent.SET_USER_ID,scMsg.userid))

    def on_packet_startMatching(self,event):
        scMsg = msg_pb2.sc_startMatching()
        scMsg.ParseFromString(event.data)
        if scMsg.result == 0:
            print ("on_packet_startMatching -- matching failure")

    def on_packet_queueStatus(self,event):
        scMsg = msg_pb2.br_queueStatus()
        scMsg.ParseFromString(event.data)
        readyNum = 0
        for user in scMsg.users:
            if user.status ==  2:
                readyNum = readyNum + 1

        self.event_dispatcher.dispatch_event(MyEvent(MyEvent.QUEUE_UPDATE, readyNum))
