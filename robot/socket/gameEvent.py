from Event import Event

class MyEvent(Event.Event):
    SET_USER_ID  = "setuserid"
    MATCH_SUCCESS = "match_success"
    READY_SUCCESS = "ready_success"
    QUEUE_UPDATE ="queue_update"
