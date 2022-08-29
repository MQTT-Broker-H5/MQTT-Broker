class c_ConnackHeader:
    def __init__(self,connectAncFlags:bool,connectReturnCode:int):
        self._ConnectAncFlags = connectAncFlags
        self._ConnectReturnCode = connectReturnCode

    def _Get_ConnectAncFlags(self):
        return self._ConnectAncFlags
    def _Get_ConnectReturnCode(self):
        return self._ConnectReturnCode

    def _Set_ConnectAncFlags(self,value):
        self._ConnectAncFlags = value

    def _Set_ConnectReturnCode(self,value):
        self._ConnectReturnCode = value

    ConnectAncFlag = property(
        fget= _Get_ConnectAncFlags,
        fset= _Set_ConnectAncFlags)

    ConnectReturnCode = property(
        fget= _Get_ConnectReturnCode,
        fset= _Set_ConnectReturnCode)





