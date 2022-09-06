class c_ContentFlagByte:
    def __init__(self,cleanSession:bool,willFlag:bool,willQoS:int,willRetain:bool,passwordFlag:bool,usernameFlag:bool):
        self._CleanSession = cleanSession
        self._WillFlag = willFlag
        self._WillQoS = willQoS
        self._WillRetain = willRetain
        self._PassworFlag = passwordFlag
        self._UsernameFlag = usernameFlag

    def _get_CleanSession(self):
        return self._CleanSession
    def _get_WillFlag(self):
        return self._WillFlag
    def _get_WillQoS(self):
        return self._WillQoS
    def _get_WillRetain(self):
        return self._WillRetain
    def _get_PassworFlag(self):
        return self._PassworFlag
    def _get_UsernameFlag(self):
        return self._UsernameFlag

    def _Set_CleanSession(self, value):
        self._CleanSession = value
    def _Set_WillFlag(self, value):
        self._WillFlag = value
    def _Set_WillQoS(self, value):
        self._WillQoS = value
    def _Set_WillRetain(self, value):
        self._WillRetain = value
    def _Set_PassworFlag(self, value):
        self._PassworFlag = value
    def _Set_UsernameFlag(self, value):
        self._UsernameFlag = value

    CleanSession = property(
        fget=_get_CleanSession,
        fset=_Set_CleanSession)

    Willflag = property(
        fget=_get_WillFlag,
        fset=_Set_WillFlag)

    WillQoS = property(
        fget=_get_WillQoS,
        fset=_Set_WillQoS)

    WillRetain = property(
        fget=_get_WillRetain,
        fset=_Set_WillRetain)

    PasswordFlag = property(
        fget=_get_PassworFlag,
        fset=_Set_PassworFlag)

    UsernameFlag = property(
        fget=_get_UsernameFlag,
        fset=_Set_UsernameFlag)




