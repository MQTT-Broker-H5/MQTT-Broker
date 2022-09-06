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

    def _Get_ClientIDLenght(self):
        return self._ClientIDLenght
    def _Get_ClientID(self):
        return self._ClientID
    def _Get_UserNameLenght(self):
        return self._UserNameLenght
    def _Get_Username(self):
        return self._Username
    def _Get_PasswordLenght(self):
        return self._PasswordLenght
    def _Get_Password(self):
        return self._Password

    def _Set_ClientIDLenght(self,value):
        self._ClientIDLenght = value
    def _Set_ClientID(self,value):
        self._ClientID = value
    def _Set_UsernameLenght(self,value):
        self._UserNameLenght = value
    def _Set_Username(self,value):
        self._Username = value
    def _Set_PasswordLenght(self,value):
        self._PasswordLenght = value
    def _Set_Password(self,value):
        self._Password = value

    ClientIDLenght = property(
        fget= _Get_ClientIDLenght,
        fset= _Set_ClientIDLenght)
    ClientID = property(
        fget= _Get_ClientID,
        fset= _Set_ClientID)
    UsernameLenght = property(
        fget= _Get_UserNameLenght,
        fset= _Set_UsernameLenght)
    Username = property(
        fget= _Get_Username,
        fset= _Set_Username)
    PasswordLenght = property(
        fget= _Get_PasswordLenght,
        fset= _Set_PasswordLenght)
    Password = property(
        fget= _Get_Password,
        fset= _Set_Password)


