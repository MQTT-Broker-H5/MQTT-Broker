from Models.Payload import c_Payload
from Models.FixHeader import c_FixHeader
from Models.VariableHeader import c_VariableHeader
class c_MQTTPacket():
    def __init__(self,fixHeader:c_FixHeader,varibleHeader:c_VariableHeader,payload:c_Payload):
        self._FixHeader = fixHeader
        self._VaribleHeader = varibleHeader
        self._Payload = payload

