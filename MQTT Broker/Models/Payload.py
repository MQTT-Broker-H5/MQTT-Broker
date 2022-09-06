from Models.UnsubscribePayload import c_UnSubscribePayload
from Models.SubackPayload import c_SubackPayload
from Models.SubscribePayload import c_SubscribePayload
from Models.ConnectPayload import c_ConnectPayload
class c_Payload:
    def __init__(self,unsubscribePayload:c_UnSubscribePayload,subackPayload:c_SubackPayload,subscribePayload:c_SubscribePayload,connectPayload:c_ConnectPayload):
        self._UnsubscribePayload = unsubscribePayload
        self._SubackPayload = subackPayload
        self._SubscribePayload = subscribePayload
        self._ConnectPayload = connectPayload