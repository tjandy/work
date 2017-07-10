
import socket, time
import threading
import client_AI

import struct
import static
import packetHandler
import packetid
import random

from Event import EventDispatcher

class robotClient (threading.Thread):
    def __init__ (self,addr,port,idx):
        threading.Thread.__init__(self)
        self.dispatcher = EventDispatcher.EventDispatcher()
        self.packethandler = packetHandler.packetHandler(self.dispatcher)
        self._ai = client_AI.AI_Control(self)
        self._dst = addr
        self._dst_port = port
        self.queue = None
        self._ai.setNick("testUser"+str(idx))
        self._ai.setDeviceId("testDeviceId"+str(idx))
        self.recvbuf=''


    def decode_socket_data(self,data):
        if data == None:
            return None
        self.recvbuf += data
        data_list = []
        buffer_size = len(self.recvbuf)
        if buffer_size < static.HEAD_LENGTH:
            return None
        try:
            code, package_len = struct.unpack('@HH', self.recvbuf[0:static.HEAD_LENGTH])
        except struct.error:
            return None

        if buffer_size == static.HEAD_LENGTH:
            # nobody
            if package_len > 0:
                return None
            data_list.append((code, None))
            self.recvbuf =  self.recvbuf[static.HEAD_LENGTH:]
            return data_list

        if package_len > len(self.recvbuf[static.HEAD_LENGTH:]):
            return  None

        elif package_len == len(self.recvbuf[static.HEAD_LENGTH:]):
            try:
                data = struct.unpack('>%ds' % package_len, self.recvbuf[static.HEAD_LENGTH:])
            except struct.error:
                return None
            data_list.append((code, data))
            self.recvbuf = self.recvbuf[static.HEAD_LENGTH+package_len:]
            return data_list

        else:
            try:
                data = struct.unpack('>%ds' % package_len, self.recvbuf[static.HEAD_LENGTH:static.HEAD_LENGTH + package_len])
            except struct.error:
                return None
            data_list.append((code, data))
            self.recvbuf = self.recvbuf[static.HEAD_LENGTH + package_len:]
            return data_list

    def encode_socket_data(self,msgid,data_buffer):
        fmt = '@HH'+str(len(data_buffer))+'s'
        buffer_size = len(data_buffer)
        msg_data    = struct.pack(fmt,msgid,buffer_size,data_buffer)
        return msg_data

    def sendMsg(self,msgid,data):
        self.tcp.send(self.encode_socket_data(msgid,data))

    def addEvent(self,event):
        self.dispatcher.dispatch_event(event)

    def _initTcp(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.connect((self._dst, self._dst_port))
        self.tcp.setblocking(False)

    def _initUDP(self):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _recvMsg(self):
        try:
            data = self.tcp.recv(static.RECV_BUFFER_SIZE)
        except:
            return
        try:
            data_list = self.decode_socket_data(data)
            if data_list != None and  data_list.__len__ > 0 :
                for _data in data_list:
                    code, message = _data
                    print(str(code))
                    self.addEvent(packetid.PacketID(code,"".join(tuple(message))))
        except Exception as e:
            print(e)
            print(data)


    def run(self):
        self._initTcp()
        self._ai.startTick()
        while True:
            try:
                self._ai.tick()
                # recv packet
                self._recvMsg()

            except Exception as e:
                print(e)
            time.sleep(1)

        self._deinit()

    def _deinit(self):
        self.tcp.shutdown(socket.SHUT_RDWR)
        # self.udp.shutdown(socket.SHUT_RDWR)

def start(ip,port):
    threads = []
    num = 1
    for idx in xrange(0, num):
        threads.append(robotClient(ip,port,random.randint(1, 10000) ))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    start(static.IP_ADDR,static.IP_PORT)
    