import sys
import re
import platform
import os
messageId =1000


java_file= os.path.join("java","CidConst.java") 
csharp_file_msg=os.path.join("csharp","cProto.cs") 
csharp_file_Serializer=os.path.join("csharp","Serializer.cs")
python_file= os.path.join("python","packetid.py") 


packetlist =''
def writePythonHead(file):
    file.write('from enum import Enum\n')
    file.write('class PacketId(Enum):\n')

def writePythonEnd(file):
    return

def writeToPython(s,python):
    code = '\t{0} = {1}\n'.format(s, messageId)
    python.write(code)


def wirteJavaHead(file):
    file.write('package com.CityCrashTaxi.server.net.protocol.comm;\n')
    file.write('import java.util.Map;\n')
    file.write('import java.util.concurrent.ConcurrentHashMap;\n')
    file.write('public class CidConst {\n')
    file.write('\tpublic static Map<Integer,String> packetList = new ConcurrentHashMap<Integer,String>();\n')
	
def writeJavaEnd(file):
    file.write('\tpublic static void initPacketList()\n')
    file.write('\t{\n')
    file.write(packetlist)
    file.write('\t}\n')
    file.write('}\n')

def writeToJava(s,java):
    code = '\tpublic final static int {0} = {1} ;\n'.format(s, messageId)
    java.write(code)
    global packetlist
    tmp = '\t\tpacketList.put({0},"{1}");\n'.format(messageId,s)
    packetlist += tmp

def wirteCSharpHead(file):
    file.write('//AUTO GENERATED FILE !!! DO NOT EDIT IT !!!!\n')
    file.write('using System;\n')
    file.write('namespace Net\n')
    file.write('{')
    file.write('        public class cProto\n')
    file.write('        {\n')
    file.write('                public enum PACKETID\n')
    file.write('                 {\n')
def writeCSharpEnd(file):
    file.write('                }\n')
    file.write('        }\n')
    file.write('}\n')
def wtireCSharpSerializerHead(file):
    file.write('''\
    //AUTO GENERATED FILE !!! DO NOT EDIT IT !!!!\n \
    using System.Collections;\n \
    using System.Collections.Generic;\n\
    using UnityEngine;\n \
    using pb = global::Google.Protobuf;\n \
    using Net;\n \
    using System.IO;\n \
    using System;\n \
    namespace Net\n \
    {\n \
        public class Serializer  {\n \
        	public static byte[] Serialize(cProto.PACKETID packetType,pb::IMessage pbmsg)\n \
	{\n \
		int index = (int)packetType;\n \
		byte[] pbbf;\n \
		using (MemoryStream ms = new MemoryStream())\n \
		{\n \
			pb::CodedOutputStream s = new pb::CodedOutputStream (ms);\n \
			pbmsg.WriteTo(s);\n \
			s.Flush();\n \
			pbbf = ms.ToArray ();\n \
			s.Dispose ();\n \
		}\n \
		byte[] outarray = new byte[sizeof(short) + sizeof(short) + pbbf.Length];\n \
        \n \
		Array.Copy (BitConverter.GetBytes ((short)index), outarray, sizeof(short));\n \
		Array.Copy (BitConverter.GetBytes ((short)pbbf.Length),0, outarray, sizeof(short),sizeof(short));\n \
		Array.Copy (pbbf, 0, outarray, sizeof(int), pbbf.Length);\n \
		return outarray;\n \
	}\n \
    			public static byte[] SerializeUDP(cProto.PACKETID packetType,pb::IMessage pbmsg)\n \
			{\n \
\n \
				byte[] pbbf;\n \
				using (MemoryStream ms = new MemoryStream())\n \
				{\n \
					pb::CodedOutputStream s = new pb::CodedOutputStream (ms);\n \
					pbmsg.WriteTo(s);\n \
					s.Flush();\n \
					pbbf = ms.ToArray ();\n \
					s.Dispose ();\n \
				}\n \
			return pbbf;\n \
			}\n \
    	public static pb::IMessage Deserialize(cProto.PACKETID packetID, byte[] data)\n \
	{\n \
		pb::IMessage msg = null;\n \
		switch(packetID)\n \
		{\n \
    ''') 
def writeToCSharpSerializer(ss,file):
    file.write("case cProto.PACKETID.{0}:\n".format(ss))
    file.write("msg = {0}.Parser.ParseFrom(data);\n".format(ss))
    file.write("break;\n")

def writeCSharpSerializerEnd(file):
    file.write(''' \
    			default:\n \
				Debug.LogError ("unknown PB Message");\n \
				break;\n \
		}		\n \
    \n \
		return msg;\n \
	}\n \
    }\n \
    }\n \
    ''')

def writeToCSharp(s,file):
    code = '\t\t\t{0} = {1} ,\n'.format(s,messageId)
    file.write(code)

def writeToFile(ss,java,csharp,csharp_Serializer,python):
    writeToJava(ss,java)
    writeToCSharp(ss,csharp)
    writeToCSharpSerializer(ss,csharp_Serializer)
    writeToPython(ss, python)
    global messageId
    messageId = messageId + 1

def writeHead(java,csharp_msg,csharp_Serializer,python):
    wirteJavaHead(java)
    wirteCSharpHead(csharp_msg)
    wtireCSharpSerializerHead(csharp_Serializer)
    writePythonHead(python)

def writeEnd(java,csharp,csharp_Serializer,python):
    writeJavaEnd(java)
    writeCSharpEnd(csharp)
    writeCSharpSerializerEnd(csharp_Serializer)
    writePythonEnd(python)

def writeContend(f,java,csharp,csharp_Serializer,python):
    list_of_all_the_lines = f.readlines()
    for line in list_of_all_the_lines:
        key = re.match(r'message (\w+){', line)
        if (key != None):
            writeToFile(key.group(1),java,csharp,csharp_Serializer,python)

def do(file_name):
    f = open(file_name,'r')
    java = open(java_file,'w')
    csharp_msg =  open(csharp_file_msg,'w')
    csharp_Serializer = open(csharp_file_Serializer,'w')
    python = open(python_file,'w')

    writeHead(java,csharp_msg,csharp_Serializer,python)
    writeContend(f,java,csharp_msg,csharp_Serializer,python)
    writeEnd(java,csharp_msg,csharp_Serializer,python)

    f.close()
    java.flush()
    java.close()
    csharp_msg.flush()
    csharp_msg.close()
    csharp_Serializer.flush()
    csharp_Serializer.close()
    python.flush()
    python.close()


def main(argv):
    filename = argv[1]
    do(filename)


if __name__ == '__main__':
    main(sys.argv)