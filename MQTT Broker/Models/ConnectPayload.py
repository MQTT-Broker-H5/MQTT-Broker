class c_ConnectPayload:
    def __init__(self,clientIDLenght:int,clientID:str,willTopicLenght:int,willTopic:str,willMessageLenght:int,willMessage:str,userNameLenght:int,userName:str,passwordLenght:int,password:str):
        self._ClientIDLenght = clientIDLenght
        self._ClientID = clientID
        self._WillTopicLenght = willTopicLenght
        self._WillTopic = willTopic
        self._WillMessageLenght = willMessageLenght
        self._WillMessage = willMessage
        self._UserNameLenght = userNameLenght
        self._Username = userName
        self._PasswordLenght = passwordLenght
        self._Password = password