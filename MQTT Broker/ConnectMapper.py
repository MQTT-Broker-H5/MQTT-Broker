from asyncio.windows_events import NULL
from Models.MQTTPacket import c_MQTTPacket
from Models.Client import c_MQTTClient
from Models.FixHeader import c_FixHeader
from Models.VariableHeader import c_VariableHeader
from Models.Payload import c_Payload
from Models.FixHeaderFlags import c_FixHeaderFlags
from Models.ConnectHeader import c_ConnectHeader
from Models.ContentFlagByte import c_ContentFlagByte
from Models.ConnectPayload import c_ConnectPayload
from MQTTHelper import c_MQTTHelper
class c_ConnectMapper():
    Helper = c_MQTTHelper()
    hexPacket = list()

    #Generates a connect client and mapps it to an c_MQTTClient obj
    #Then we return it to the ClientManager
    def GenereateConnectClient(self,packet):
        self.hexPacket = self.Helper.ConvertDecimalToHex(packet)
        fixheader = c_FixHeader(self.Helper.GetCommand(packet),c_FixHeaderFlags(NULL,NULL,NULL),int(self.hexPacket[1],16))
        self.hexPacket = self.Helper.RemoveFromPacket(self.hexPacket,2)
        PNlenght = self.CombindInt(self.hexPacket,2)
        varibleheader = c_VariableHeader(c_ConnectHeader(PNlenght,self.GetString(self.hexPacket,PNlenght),self.GetLenght(self.hexPacket[0]),self.GetContentFlagByte(self.hexPacket),self.CombindInt(self.hexPacket,2)),NULL,NULL,NULL)
        payload = c_Payload(NULL,NULL,NULL,self.GenerateConnectPayload(self.hexPacket,varibleheader))
        client = c_MQTTClient(c_MQTTPacket(fixheader,varibleheader,payload))
        return client


    #TODO Generate payload dose not work in case of usernameflag is not set.. LOOK IN TO THIS
    #TODO If clientID == 0 Generate random id

    #Generats the payload for the connect client
    #Mapps it and returns c_ConnectPayload obj
    def GenerateConnectPayload(self,packet,varibleheader:c_VariableHeader):
        clientIdLenght = self.CombindInt(packet,2)
        clientId = self.GetString(packet,clientIdLenght)
        if varibleheader._ConnectHeader._ContentFlagByte.Willflag == True:
            willTopicLenght = self.CombindInt(packet,2)
            willTopic = self.GetString(packet,willTopicLenght)
            willMessageLenght = self.CombindInt(packet,2)
            willMessage = self.GetString(packet,willMessageLenght)
        if varibleheader._ConnectHeader._ContentFlagByte.UsernameFlag == True:
            usernameLenght = self.CombindInt(packet,2)
            username = self.GetString(packet,usernameLenght)
        if varibleheader._ConnectHeader._ContentFlagByte.PasswordFlag == True:
            passwordLenght = self.CombindInt(packet,2)
            password = self.GetString(packet,passwordLenght)
        return c_ConnectPayload(clientIdLenght,clientId,willTopicLenght,willTopic,willMessageLenght,willMessage,usernameLenght,username,passwordLenght,password)

    #Returns a string value based on the lenght
    #Lenght determens how much of the packet we would like from start of the packet
    #Removes the part of the packet we converted
    def GetString(self,packet,lenght):
        byte = []
        for x  in range(lenght):
            byte.append(int(packet[x],16))
        temp = bytes(byte).decode('utf-8')
        self.Helper.RemoveFromPacket(self.hexPacket,lenght)
        return temp

    #Converts the packet to int and returns it
    #Removes the part of the packet we converted
    def GetLenght(self,packet):
        lenght = int(packet,16)
        self.Helper.RemoveFromPacket(self.hexPacket,NULL)
        return lenght

    #Retusn an integer based on the packet and lenght
    #Lenght determens how much of the packet we wont to combind
    #Removes the part of the packet we converted
    def CombindInt(self,packet,lenght):
        newLenght = 0
        for i in range(0,lenght):
            newLenght += int(packet[i],16)
        self.Helper.RemoveFromPacket(self.hexPacket,lenght)
        return newLenght

    #Checks through an arry of the bit values that are set in the will flags
    #Then generates an WillFlagsObj with the values that we return
    def GetContentFlagByte(self,packet):
        WillQoS = 0
        setFlags = self.Helper.LeftBitwiseCheckFlags(int(packet[0],16))
        self.Helper.RemoveFromPacket(self.hexPacket,NULL)
        if setFlags[1] == 1:
            CleanSession = True
        elif setFlags[1] != 1:
            CleanSession = False
        if setFlags[2] == 1:
            Willflag = True
        elif setFlags[2] != 1:
            Willflag = False
        if setFlags[3] == 1 and setFlags[4] != 1:
            WillQoS = 1
        elif setFlags[3] != 1 and setFlags[4] == 1:
            WillQoS = 2
        elif setFlags[3] == 0 and setFlags[4] == 0:
            WillQoS = 0
        if setFlags[5] == 1:
            WillRetain = True
        elif setFlags[5] != 1:
            WillRetain = False
        if setFlags[6] == 1:
            PasswordFlag = True
        elif setFlags[6] != 1:
            PasswordFlag = False
        if setFlags[7] == 1:
            UsernameFlag = True
        elif setFlags[7] != 1:
            UsernameFlag = False
        return c_ContentFlagByte(CleanSession,Willflag,WillQoS,WillRetain,PasswordFlag,UsernameFlag)