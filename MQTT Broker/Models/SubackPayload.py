class c_SubackPayload:
    def __init__(self,returnCode:list):
        self._ReturnCode = returnCode

    def _Get_ReturnCode(self):
        return self._ReturnCode

    def _Set_ReturnCode(self,value):
        self._ReturnCode = value

    ReturnCode = property(
        fget= _Get_ReturnCode,
        fset= _Set_ReturnCode)




