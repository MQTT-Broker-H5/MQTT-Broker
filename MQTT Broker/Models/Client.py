from Models.MQTTPacket import c_MQTTPacket
class c_MQTTClient:
    def __init__(self,mqtttPacket:c_MQTTPacket):
        self._MQTTPacket = mqtttPacket

    def _Get_MQTTPacket(self):
        return self._MQTTPacket
    def _Set_MQTTPacket(self,value):
        self._MQTTPacket = value

    MQTTPacket = property(
        fget= _Get_MQTTPacket,
        fset= _Set_MQTTPacket)
