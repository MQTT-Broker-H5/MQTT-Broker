class c_ContentFlagByte:
    def __init__(self,cleanSession:bool,willFlag:bool,willQoS:int,willRetain:bool,passwordFlag:bool,usernameFlag:bool):
        self._CleanSession = cleanSession
        self._WillFlag = willFlag
        self._WillQoS = willQoS
        self._WillRetain = willRetain
        self._PassworFlag = passwordFlag
        self._UsernameFlag = usernameFlag


