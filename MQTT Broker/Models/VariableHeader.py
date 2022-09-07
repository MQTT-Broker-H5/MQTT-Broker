from Models.ConnectHeader import c_ConnectHeader
from Models.ConnackHeader import c_ConnackHeader
from Models.PublishHeader import c_PublishHeader
from Models.PubackHeader import c_PubackHeader
class c_VariableHeader:
    def __init__(self,connectHeader:c_ConnectHeader,connackHeader:c_ConnackHeader,publishHeader:c_PublishHeader,pubackHeader:c_PubackHeader):
        self._ConnectHeader = connectHeader
        self._ConnackHeader = connackHeader
        self._PublishHeader = publishHeader
        self._PubackHeader = pubackHeader
