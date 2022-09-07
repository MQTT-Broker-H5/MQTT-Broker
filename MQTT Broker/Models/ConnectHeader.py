from Models.ContentFlagByte import c_ContentFlagByte
class c_ConnectHeader:
    def __init__(self,protocolNameLenght:int,protocolName:str,protocolLevel:int,contentFlagByte:c_ContentFlagByte,keepAlive:int):
        self._ProtocolNameLenght = protocolNameLenght
        self._ProtocolName = protocolName
        self._ProtocolLevel = protocolLevel
        self._ContentFlagByte = contentFlagByte
        self._KeepAlive = keepAlive
