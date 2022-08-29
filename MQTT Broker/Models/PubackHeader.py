class c_PubackHeader:
    def __init__(self,packetIdentifer:int):
        self._PacketIdentifer = packetIdentifer

    def _Get_PacketIdentifer(self):
        return self._PacketIdentifer

    def _Set_PacketIdentifer(self,value):
        self._PacketIdentifer = value

    PacketIdentifer = property(
        fget= _Get_PacketIdentifer)




