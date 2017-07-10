
import msg_pb2
from  gameEvent import MyEvent

class eventHandler(object):
    def __init__(self,event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.event_dispatcher.add_event_listener(MyEvent.LOGIN,self.on_event_LOGIN)
        self.event_dispatcher.add_event_listener(MyEvent.MATCH, self.on_event_MATCH)
        self.event_dispatcher.add_event_listener(MyEvent.READY, self.on_event_READY)

    def on_event_LOGIN(self,event):
        print("receive event %s",event.type);
        msg = msg_pb2.cs_loginGame()
        msg.deviceid ="121211111"
        msg.nick='test'
        event.data.sendMsg(1000,msg.SerializeToString())


    def on_event_MATCH(self, event):
        print("receive event %s", event.data)

    def on_event_READY(self, event):
        print("receive event %s", event.data)