from Models.MQTTPacket import c_MQTTPacket
import socket
class c_MQTTClient:



    def __init__(self,mqtttPacket:c_MQTTPacket, socket: socket.socket):
        self._MQTTPacket = mqtttPacket
        self._socket = socket
                


