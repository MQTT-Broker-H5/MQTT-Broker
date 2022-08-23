class MQTTPacket:
    def __init__(self,fixHeader,varibleHeader,payload):
        self._FixHeader = fixHeader
        self._VaribleHeader = varibleHeader
        self._Payload = payload

    def _Get_FixHeader(self):
        return self._FixHeader
    def _Get_VaribleHeader(self):
        return self._VaribleHeader
    def _Get_Payload(self):
        return self._Payload

    def _Set_FixHeader(self,value):
        self._FixHeader = value
    def _Set_VaribleHeader(self,value):
        self._VaribleHeader = value
    def _Set_Payload(self,value):
        self._Payload = value

    FixHeader = property(
        fget= _Get_FixHeader,
        fset= _Set_FixHeader)
    VaribleHeader = property(
        fget= _Get_FixHeader,
        fset= _Set_FixHeader)
    Payload = property(
        fget= _Get_Payload,
        fset= _Set_Payload)




