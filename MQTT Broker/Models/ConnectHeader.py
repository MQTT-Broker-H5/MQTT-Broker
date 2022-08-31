from Models.ContentFlagByte import c_ContentFlagByte
class c_ConnectHeader:
    def __init__(self,protocolNameLenght:int,protocolName:str,protocolLevel:int,contentFlagByte:c_ContentFlagByte,keepAlive:int):
        self._ProtocolNameLenght = protocolNameLenght
        self._ProtocolName = protocolName
        self._ProtocolLevel = protocolLevel
        self._ContentFlagByte = contentFlagByte
        self._KeepAlive = keepAlive

    def _Get_ProtocolNameLenght(self):
        return self._ProtocolNameLenght
    def _Get_ProtocolName(self):
        return self._ProtocolName
    def _Get_ProtocolLevel(self):
        return self._ProtocolLevel
    def _Get_ContentFlagByte(self):
        return self._ContentFlagByte
    def _Get_KeepAlive(self):
        return self._KeepAlive

    def _Set_ProtocolNameLenght(self, value):
        self._ProtocolNameLenght = value
    def _Set_ProtocolName(self, value):
        self._ProtocolName = value
    def _Set_ProtocolLevel(self, value):
        self._ProtocolLevel = value
    def _Set_ContentFlagByte(self, value):
        self._ContentFlagByte = value
    def _Set_KeepAlive(self, value):
        self._KeepAlive = value

    ProtocolNameLenght = property(
        fget=_Get_ProtocolNameLenght,
        fset=_Set_ProtocolNameLenght)

    ProtocolName = property(
        fget=_Get_ProtocolName,
        fset=_Set_ProtocolName)

    ProtocolLevel = property(
        fget=_Get_ProtocolLevel,
        fset=_Set_ProtocolLevel)

    ContentFlagByte = property(
        fget=_Get_ContentFlagByte,
        fset=_Set_ContentFlagByte)

    KeepAlive = property(
        fget=_Get_KeepAlive,
        fset=_Set_KeepAlive)
