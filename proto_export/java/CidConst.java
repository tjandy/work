package com.CityCrashTaxi.server.net.protocol.comm;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
public class CidConst {
	public static Map<Integer,String> packetList = new ConcurrentHashMap<Integer,String>();
	public final static int cs_loginGame = 1000 ;
	public final static int sc_loginGame = 1001 ;
	public final static int userInfo = 1002 ;
	public final static int br_queueStatus = 1003 ;
	public final static int cs_startMatching = 1004 ;
	public final static int sc_startMatching = 1005 ;
	public final static int cs_exitMatching = 1006 ;
	public final static int sc_exitMatching = 1007 ;
	public final static int cs_ready = 1008 ;
	public final static int sc_ready = 1009 ;
	public final static int userLoadingInfo = 1010 ;
	public final static int cs_loading = 1011 ;
	public final static int br_loading = 1012 ;
	public final static int playerInfo = 1013 ;
	public final static int objectInfo = 1014 ;
	public final static int br_ObjectUpdate = 1015 ;
	public final static int br_startGame = 1016 ;
	public final static int cs_pickUpItem = 1017 ;
	public final static int sc_pickUpItmeResult = 1018 ;
	public final static int br_pickUpItem = 1019 ;
	public final static int cs_useItem = 1020 ;
	public final static int sc_useItemResult = 1021 ;
	public final static int br_useItem = 1022 ;
	public final static int cs_pickupNpc = 1023 ;
	public final static int sc_pickupNpcResult = 1024 ;
	public final static int br_pickupNpc = 1025 ;
	public final static int cs_npcArrive = 1026 ;
	public final static int sc_npcArriveResult = 1027 ;
	public final static int br_npcArrive = 1028 ;
	public final static int cs_crashCar = 1029 ;
	public final static int sc_crashCarResult = 1030 ;
	public final static int br_crashCar = 1031 ;
	public final static int br_carreborn = 1032 ;
	public final static int mathVector3 = 1033 ;
	public final static int cs_syncPos = 1034 ;
	public final static int br_syncPos = 1035 ;
	public final static int cs_regist = 1036 ;
	public final static int sc_regist = 1037 ;
	public final static int cs_matchInfo = 1038 ;
	public final static int matchInfo = 1039 ;
	public final static int br_matchInfo = 1040 ;
	public final static int br_matchResult = 1041 ;
	public static void initPacketList()
	{
		packetList.put(1000,"cs_loginGame");
		packetList.put(1001,"sc_loginGame");
		packetList.put(1002,"userInfo");
		packetList.put(1003,"br_queueStatus");
		packetList.put(1004,"cs_startMatching");
		packetList.put(1005,"sc_startMatching");
		packetList.put(1006,"cs_exitMatching");
		packetList.put(1007,"sc_exitMatching");
		packetList.put(1008,"cs_ready");
		packetList.put(1009,"sc_ready");
		packetList.put(1010,"userLoadingInfo");
		packetList.put(1011,"cs_loading");
		packetList.put(1012,"br_loading");
		packetList.put(1013,"playerInfo");
		packetList.put(1014,"objectInfo");
		packetList.put(1015,"br_ObjectUpdate");
		packetList.put(1016,"br_startGame");
		packetList.put(1017,"cs_pickUpItem");
		packetList.put(1018,"sc_pickUpItmeResult");
		packetList.put(1019,"br_pickUpItem");
		packetList.put(1020,"cs_useItem");
		packetList.put(1021,"sc_useItemResult");
		packetList.put(1022,"br_useItem");
		packetList.put(1023,"cs_pickupNpc");
		packetList.put(1024,"sc_pickupNpcResult");
		packetList.put(1025,"br_pickupNpc");
		packetList.put(1026,"cs_npcArrive");
		packetList.put(1027,"sc_npcArriveResult");
		packetList.put(1028,"br_npcArrive");
		packetList.put(1029,"cs_crashCar");
		packetList.put(1030,"sc_crashCarResult");
		packetList.put(1031,"br_crashCar");
		packetList.put(1032,"br_carreborn");
		packetList.put(1033,"mathVector3");
		packetList.put(1034,"cs_syncPos");
		packetList.put(1035,"br_syncPos");
		packetList.put(1036,"cs_regist");
		packetList.put(1037,"sc_regist");
		packetList.put(1038,"cs_matchInfo");
		packetList.put(1039,"matchInfo");
		packetList.put(1040,"br_matchInfo");
		packetList.put(1041,"br_matchResult");
	}
}