import string
from Models.FixHeaderFlags import c_FixHeaderFlags
class c_FixHeader:
    def __init__(self,command:string,fixHeaderFlags:c_FixHeaderFlags,protocolLenght:int):
        self._Command = command
        self._FixHeaderFlags = fixHeaderFlags
        self._ProtocolLenght = protocolLenght
