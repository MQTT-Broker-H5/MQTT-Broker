class ConnectHeader:
    def __init__(self,protocolName,protocolLevel,contentFlagByte,keepAlive):
        self._ProtocolName = protocolName
        self._ProtocolLevel = protocolLevel
        self._ContentFlagByte = contentFlagByte
        self._KeepAlive = keepAlive

    def _Get_ProtocolName(self):
        return self._ProtocolName
    def _Get_ProtocolLevel(self):
        return self._ProtocolLevel
    def _Get_ContentFlagByte(self):
        return self._ContentFlagByte
    def _Get_KeepAlive(self):
        return self._KeepAlive

    def _Set_ProtocolName(self, value):
        self._ProtocolName = value
    def _Set_ProtocolLevel(self, value):
        self._ProtocolLevel = value
    def _Set_ContentFlagByte(self, value):
        self._ContentFlagByte = value
    def _Set_KeepAlive(self, value):
        self._KeepAlive = value

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
