import websocket
import threading
import time
import sys
import random
import json
from message.Message import PackArgument
from message.Message import initPack
from message.Message import unPacketMesage

def enum(**enums):
    return type('Enum', (), enums)
Numbers = enum( INIT=1, CONNECT=2, LOGIN=3,ENTERROOM=4,CLOSE=5 )

clientState= Numbers.INIT
isHost = False
emptySeat = set([0, 1, 2, 6, 7, 8])
aliveSeat = [0,1,2,6,7,8]
mySeat = -1
myRoleType = 0
platformId = -1

def resetInitData():
    global clientState
    global emptySeat
    global aliveSeat
    global myRoleType
    emptySeat = set([0, 1, 2, 6, 7, 8])
    aliveSeat = [0, 1, 2, 6, 7, 8]
    myRoleType = 0



def addSeatFlag(seat):
    global emptySeat
    emptySeat.add(seat)

def markSeatFlag(seat):
    global emptySeat
    if isinstance(seat,int):
        emptySeat.remove(seat)
    elif isinstance(seat,list):
        for item  in seat:
            emptySeat.remove(item)

def checkCanStartGame():
    if isHost :
        if emptySeat.__len__() == 0:
            return True
    return False

def kickSomeOne(msg):
    if isinstance(msg,int):
        if msg == mySeat:
            return
        aliveSeat.remove(msg)

def on_message(ws, message):

    global clientState
    global isHost
    module=0
    msgid =1
    body = ""
    try:
        module, msgid, body = unPacketMesage(message)
    except Exception, e:
        print Exception, ":", e
        clientState = Numbers.CLOSE
        return

    data = json.loads(body)

    if module != 1:
        print module,msgid,body

    if module == 2 and msgid ==1 :
        sendMatchRoom(ws)
        global platformId
        platformId = data['content']['platformId']
        print data['content']['platformId']
    elif module ==3 and msgid ==4:
        print data['content']['joinRoomVo']
        global mySeat
        if data['content']['joinRoomVo'] == None :
            isHost = True
            #markSeatFlag(data['content']['createRoomVo']['closeSeats'])
            markSeatFlag(data['content']['createRoomVo']['slot'])
            mySeat = data['content']['createRoomVo']['slot']
        else:
            for seats in data['content']['joinRoomVo']['seatVos']:
                if seats['state'] == 2 :
                    markSeatFlag(seats['slot'])
                    if seats['playerVo']['platformId'] == platformId:
                        mySeat = seats['slot']

        clientState = Numbers.ENTERROOM
    elif module ==4 and msgid ==-2 :
        markSeatFlag(data['slot'])
        if checkCanStartGame():
            sendStartGame(ws)
    elif module ==4 and msgid == -3:
        addSeatFlag(data['slot'])
    elif module == 4 and msgid == -5:
        global myRoleType
        for i in data['roleVos']:
            if i['slot'] ==  mySeat:
                myRoleType = i['roleType']
                print 'myRoleType %d '% myRoleType
            kickSomeOne(i['slot'])
    elif module == 4 and msgid == -6:
        if myRoleType ==  1:
            sendWolfKill(ws)
    elif module ==4  and msgid == -19:
        if data['type'] == 1:
            kickSomeOne(data['dies'][0]['slot'])
    elif module == 4 and msgid == -22:
        if data['slot'] == mySeat:
            sendpassLastWords(ws)
    elif module == 4 and msgid == -31:
        if data['slot'] == mySeat:
            sendDayPass(ws)
    elif module == 5 and msgid == -2:
        resetInitData()
        sendReady(ws)
        markSeatFlag(mySeat)
    elif module == 4 and msgid == -28:
        markSeatFlag(data['slot'])
        if checkCanStartGame():
            sendStartGame(ws)

def on_error(ws, error):
    global clientState
    clientState = Numbers.CLOSE
    print(error)

def on_close(ws):
    global clientState
    clientState = Numbers.CLOSE
    print("### closed ###")

def sendReady(ws):
    msg = PackArgument()
    msg.append('{"op":2}')
    buff = initPack(4, 19, msg.content)
    ws.send(buff)

def sendDayPass(ws):
    msg = PackArgument()
    msg.append('{}')
    buff = initPack(4, 16, msg.content)
    ws.send(buff)

def sendpassLastWords(ws):
    msg = PackArgument()
    msg.append('{}')
    buff = initPack(4, 22, msg.content)
    ws.send(buff)

def sendStartGame(ws):
    msg = PackArgument()
    msg.append('{}')
    buff = initPack(4, 5, msg.content)
    ws.send(buff)

def sendWolfKill(ws):
    msg = PackArgument()
    msg.append('{"op":1,"slot":%d}' % aliveSeat[-1] )
    buff = initPack(4, 6, msg.content)
    ws.send(buff)

def sendAuth(ws):
    momoid = random.randint(1,1000)
    msg = PackArgument()
    json = '{"token":"%s"}' % (momoid)
    print json
    msg.append(json)
    buff = initPack(2,1, msg.content)
    ws.send(buff)
def sendMatchRoom(ws):
    msg = PackArgument()
    msg.append('{"roomType":3}')
    buff = initPack(3, 4, msg.content)
    ws.send(buff)

def sendPing(ws):
    msg = PackArgument()
    msg.append('{}')
    buff = initPack(1, 1,msg.content)
    ws.send(buff)

def on_open(ws):
    global clientState
    clientState = Numbers.CONNECT
    def run():
        sendAuth(ws)
        global clientState
        while clientState != Numbers.CLOSE:
            if clientState == Numbers.ENTERROOM:
                sendPing(ws)

            time.sleep(10)
        ws.close()
    t = threading.Thread(target=run, args=())
    t.start()

def start(host):
    ws = websocket.WebSocketApp(host,on_message=on_message,on_error=on_error,on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

	
if __name__ == "__main__":
    if len(sys.argv) < 2:
        host = "ws://192.168.2.58:8999/";
       # host = "ws://47.92.105.64:12306/";
        #host = "ws://192.168.2.31:12306/";
        # host = "ws://123.114.126.231:8999/";

    else:
        host = sys.argv[1]
    start(host);
