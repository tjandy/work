from Event import Event

class PacketID(Event.Event):
	cs_loginGame = 1000
	sc_loginGame = 1001
	userInfo = 1002
	br_queueStatus = 1003
	cs_startMatching = 1004
	sc_startMatching = 1005
	cs_exitMatching = 1006
	sc_exitMatching = 1007
	cs_ready = 1008
	sc_ready = 1009
	userLoadingInfo = 1010
	cs_loading = 1011
	br_loading = 1012
	playerInfo = 1013
	objectInfo = 1014
	br_ObjectUpdate = 1015
	br_startGame = 1016
	cs_pickUpItem = 1017
	sc_pickUpItmeResult = 1018
	br_pickUpItem = 1019
	cs_useItem = 1020
	sc_useItemResult = 1021
	br_useItem = 1022
	cs_pickupNpc = 1023
	sc_pickupNpcResult = 1024
	br_pickupNpc = 1025
	cs_npcArrive = 1026
	sc_npcArriveResult = 1027
	br_npcArrive = 1028
	cs_crashCar = 1029
	sc_crashCarResult = 1030
	br_crashCar = 1031
	br_carreborn = 1032
	mathVector3 = 1033
	cs_syncPos = 1034
	br_syncPos = 1035
	cs_regist = 1036
	sc_regist = 1037
	cs_matchInfo = 1038
	matchInfo = 1039
	br_matchInfo = 1040
	br_matchResult = 1041
