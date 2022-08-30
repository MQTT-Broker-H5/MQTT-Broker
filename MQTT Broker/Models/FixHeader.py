import string
from Models.FixHeaderFlags import c_FixHeaderFlags
class c_FixHeader:
    def __init__(self,command:string,fixHeaderFlags:c_FixHeaderFlags,protocolLenght:int):
        self._Command = command
        self._FixHeaderFlags = fixHeaderFlags
        self._ProtocolLenght = protocolLenght

    def _Get_Command(self):
        return self._Command
    def _Get_FixHeaderFlag(self):
        return self._FixHeaderFlags
    def _Get_ProtocolLenght(self):
        return self._ProtocolLenght

    def _Set_Command(self,value):
        self._Command = value
    def _Set_FixHeaderFlag(self,value):
        self._FixHeaderFlags = value
    def _Set_ProtocolLenght(self,value):
        self._ProtocolLenght = value

    Command = property(
        fget= _Get_Command,
        fset= _Set_Command)
    FixHeaderFlags = property(
        fget= _Get_FixHeaderFlag,
        fset= _Set_FixHeaderFlag)
    ProtocolLenght = property(
        fget= _Get_ProtocolLenght,
        fset= _Set_ProtocolLenght)




