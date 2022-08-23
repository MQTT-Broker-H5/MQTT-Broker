class Payload:
    def __init__(self,unsubscribePayload,subackPayload,subscribePayload,connectPayload):
        self._UnsubscribePayload = unsubscribePayload
        self._SubackPayload = subackPayload
        self._SubscribePayload = subscribePayload
        self._ConnectPayload = connectPayload

    def _Get_UnsubscribePayload(self):
        return self._UnsubscribePayload
    def _Get_SubackPayload(self):
        return self._SubackPayload
    def _Get_SubscribePayload(self):
        return self._SubscribePayload
    def _Get_ConnectPayload(self):
        return self._ConnectPayload

    def _Set_UnsubscribePayload(self,value):
        self._UnsubscribePayload = value
    def _Set_SubackPayload(self,value):
        self._SubackPayload = value
    def _Set_SubscribePayload(self,value):
        self._SubscribePayload = value
    def _Set_ConnectPayload(self,value):
        self._ConnectPayload = vaue

    UnsubcribePayload = property(
        fget= _Get_UnsubscribePayload,
        fset= _Set_UnsubscribePayload)
    SubackPayload = property(
        fget= _Get_SubackPayload,
        fset= _Set_SubackPayload)
    SubscribePayload = property(
        fget= _Get_SubscribePayload,
        fset= _Set_SubscribePayload)
    ConnectPayload = property(
        fget= _Get_ConnectPayload,
        fset= _Set_ConnectPayload)




