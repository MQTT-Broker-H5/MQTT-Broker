class FixHeaderFlags:
    def __init__(self,dup,qos,retain):
        self._DUP = dup
        self._QoS = qos
        self._Retain = retain

    def _Get_DUP(self):
        return self._DUP
    def _Get_QoS(self):
        return self._QoS
    def _Get_Retain(self):
        return self._Retain

    def _Set_DUP(self,value):
        self._DUP = value
    def _Set_QoS(self,value):
        self._QoS = value
    def _Set_Retain(self,value):
        self._Retain = value

    DUP = property(
        fget= _Get_DUP,
        fset= _Set_DUP)
    QoS = property(
        fget= _Get_QoS,
        fset= _Set_QoS)
    Retain = property(
        fget= _Get_Retain,
        fset= _Set_Retain)





