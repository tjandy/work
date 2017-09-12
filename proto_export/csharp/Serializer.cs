    //AUTO GENERATED FILE !!! DO NOT EDIT IT !!!!
     using System.Collections;
     using System.Collections.Generic;
    using UnityEngine;
     using pb = global::Google.Protobuf;
     using Net;
     using System.IO;
     using System;
     namespace Net
     {
         public class Serializer  {
         	public static byte[] Serialize(cProto.PACKETID packetType,pb::IMessage pbmsg)
 	{
 		int index = (int)packetType;
 		byte[] pbbf;
 		using (MemoryStream ms = new MemoryStream())
 		{
 			pb::CodedOutputStream s = new pb::CodedOutputStream (ms);
 			pbmsg.WriteTo(s);
 			s.Flush();
 			pbbf = ms.ToArray ();
 			s.Dispose ();
 		}
 		byte[] outarray = new byte[sizeof(short) + sizeof(short) + pbbf.Length];
         
 		Array.Copy (BitConverter.GetBytes ((short)index), outarray, sizeof(short));
 		Array.Copy (BitConverter.GetBytes ((short)pbbf.Length),0, outarray, sizeof(short),sizeof(short));
 		Array.Copy (pbbf, 0, outarray, sizeof(int), pbbf.Length);
 		return outarray;
 	}
     			public static byte[] SerializeUDP(cProto.PACKETID packetType,pb::IMessage pbmsg)
 			{
 
 				byte[] pbbf;
 				using (MemoryStream ms = new MemoryStream())
 				{
 					pb::CodedOutputStream s = new pb::CodedOutputStream (ms);
 					pbmsg.WriteTo(s);
 					s.Flush();
 					pbbf = ms.ToArray ();
 					s.Dispose ();
 				}
 			return pbbf;
 			}
     	public static pb::IMessage Deserialize(cProto.PACKETID packetID, byte[] data)
 	{
 		pb::IMessage msg = null;
 		switch(packetID)
 		{
     case cProto.PACKETID.cs_loginGame:
msg = cs_loginGame.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_loginGame:
msg = sc_loginGame.Parser.ParseFrom(data);
break;
case cProto.PACKETID.userInfo:
msg = userInfo.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_queueStatus:
msg = br_queueStatus.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_startMatching:
msg = cs_startMatching.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_startMatching:
msg = sc_startMatching.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_exitMatching:
msg = cs_exitMatching.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_exitMatching:
msg = sc_exitMatching.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_ready:
msg = cs_ready.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_ready:
msg = sc_ready.Parser.ParseFrom(data);
break;
case cProto.PACKETID.userLoadingInfo:
msg = userLoadingInfo.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_loading:
msg = cs_loading.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_loading:
msg = br_loading.Parser.ParseFrom(data);
break;
case cProto.PACKETID.playerInfo:
msg = playerInfo.Parser.ParseFrom(data);
break;
case cProto.PACKETID.objectInfo:
msg = objectInfo.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_ObjectUpdate:
msg = br_ObjectUpdate.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_startGame:
msg = br_startGame.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_pickUpItem:
msg = cs_pickUpItem.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_pickUpItmeResult:
msg = sc_pickUpItmeResult.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_pickUpItem:
msg = br_pickUpItem.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_useItem:
msg = cs_useItem.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_useItemResult:
msg = sc_useItemResult.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_useItem:
msg = br_useItem.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_pickupNpc:
msg = cs_pickupNpc.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_pickupNpcResult:
msg = sc_pickupNpcResult.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_pickupNpc:
msg = br_pickupNpc.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_npcArrive:
msg = cs_npcArrive.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_npcArriveResult:
msg = sc_npcArriveResult.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_npcArrive:
msg = br_npcArrive.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_crashCar:
msg = cs_crashCar.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_crashCarResult:
msg = sc_crashCarResult.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_crashCar:
msg = br_crashCar.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_carreborn:
msg = br_carreborn.Parser.ParseFrom(data);
break;
case cProto.PACKETID.mathVector3:
msg = mathVector3.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_syncPos:
msg = cs_syncPos.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_syncPos:
msg = br_syncPos.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_regist:
msg = cs_regist.Parser.ParseFrom(data);
break;
case cProto.PACKETID.sc_regist:
msg = sc_regist.Parser.ParseFrom(data);
break;
case cProto.PACKETID.cs_matchInfo:
msg = cs_matchInfo.Parser.ParseFrom(data);
break;
case cProto.PACKETID.matchInfo:
msg = matchInfo.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_matchInfo:
msg = br_matchInfo.Parser.ParseFrom(data);
break;
case cProto.PACKETID.br_matchResult:
msg = br_matchResult.Parser.ParseFrom(data);
break;
     			default:
 				Debug.LogError ("unknown PB Message");
 				break;
 		}		
     
 		return msg;
 	}
     }
     }
     