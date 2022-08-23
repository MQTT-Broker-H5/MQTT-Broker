class PublishHeader:
    def __init__(self,topicName,packetIdentifer):
        self._TopicName = topicName
        self._PacketIdentifer = packetIdentifer

    def _Get_TopicName(self):
        return self._TopicName
    def _Get_PacketIdentifer(self):
        return self._PacketIdentifer

    def _Set_TopicName(self,value):
        self._TopicName = value
    def _Set_PacketIdentifer(self,value):
        self._PacketIdentifer = value

    TopicName = property(
        fget= _Get_TopicName,
        fset= _Set_TopicName)

    PacketIdentifer = property(
        fget= _Get_PacketIdentifer,
        fset= _Set_PacketIdentifer)




