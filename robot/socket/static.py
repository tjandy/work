


def enum(**enums):
    return type('Enum', (), enums)

HEAD_LENGTH = 4
RECV_BUFFER_SIZE=1024

ROMM_TYPE = 1
ROOM_NUM = 2
IP_ADDR = '127.0.0.1'
IP_PORT = 10010