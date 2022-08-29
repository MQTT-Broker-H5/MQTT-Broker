from ConnectHeader import c_ConnectHeader
from ConnackHeader import c_ConnackHeader
from PublishHeader import c_PublishHeader
from PubackHeader import c_PubackHeader
class c_VariableHeader:
    def __init__(self,connectHeader:c_ConnectHeader,connackHeader:c_ConnackHeader,publishHeader:c_PublishHeader,pubackHeader:c_PubackHeader):
        self._ConnectHeader = connectHeader
        self._ConnackHeader = connackHeader
        self._PublishHeader = publishHeader
        self._PubackHeader = pubackHeader

    def _Get_ConnectHeader(self):
        return self._ConnackHeader
    def _Get_ConnackHeader(self):
        return self._ConnackHeader
    def _Get_PublishHeader(self):
        return self._PublishHeader
    def _Get_PubackHeader(self):
        return self._PubackHeader

    def _Set_ConnectHeader(self,value):
        self._ConnectHeader = value
    def _Set_ConnackHeader(self,value):
        self._ConnackHeader = value
    def _Set_PublishHeader(self,value):
        self._PublishHeader = value
    def _Set_PubackHeader(self,value):
        self._Set_PubackHeader = value

    ConnectHeader = property(
        fget= _Get_ConnectHeader,
        fset= _Set_ConnectHeader)
    ConnackHeader = property(
        fget= _Get_ConnectHeader,
        fset= _Set_ConnectHeader)
    PublishHeader = property(
        fget= _Get_PublishHeader,
        fset= _Set_PublishHeader)
    PubackHeader = property(
        fget= _Get_PubackHeader,
        fset= _Get_PubackHeader)



