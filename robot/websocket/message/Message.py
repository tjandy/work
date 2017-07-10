import struct

class PackArgument():
    length = 0
    content = ""
    def append(self, cont, num=0):
        if (num == 0):
            self.content += bytes(cont) + '\x00'
        else:
            fmt = 'b'
            if (num == 2):
                fmt = 'h'
            elif num == 4:
                fmt = 'i'
            cont = struct.pack(fmt, cont)
            cont = cont[::-1]
            self.content += cont


def packMessageHeader(module,msgid):
    packed = struct.pack('b', 0)
    packed+= struct.pack('b',0)
    packed += struct.pack('h', 0)
    packed += struct.pack('h', 1)
    packed += struct.pack('b', module)
    packed += struct.pack('b', msgid)
    return packed

def initPack(module,msgid, content):
    packed = packMessageHeader(module,msgid)
    packed += content.rstrip()
    return packed

def unPacketMesage(message):
    tmp = (message[2:6])
    conLen = struct.unpack('!i', tmp)
    tmp = message[6:14]
    aa,bb,cc,dd,module,msgid = struct.unpack('bbhhbb', tmp)
    fmt = '%ds' % (int(conLen[0])-14)
    body =  struct.unpack(fmt,message[14:])
    return  module,msgid,(body.__str__())[2:-3]