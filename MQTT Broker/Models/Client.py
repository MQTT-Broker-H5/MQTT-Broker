class Client:
    def _init__(self,mqttPacket):
        self._MQTTPacket = mqttPacket

    def _Get_MQTTPacket(self):
        return self._MQTTPacket
    def _Set_MQTTPacket(self,value):
        self._MQTTPacket = value

    MQTTPacket = property(
        fget= _Get_MQTTPacket,
        fset= _Set_MQTTPacket)




