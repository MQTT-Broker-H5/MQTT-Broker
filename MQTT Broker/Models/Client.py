from Models.MQTTPacket import c_MQTTPacket
class c_MQTTClient:
    def __init__(self,mqtttPacket:c_MQTTPacket):
        self._MQTTPacket = mqtttPacket
