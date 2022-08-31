from asyncio.windows_events import NULL
from struct import pack
from Models.MQTTPacket import c_MQTTPacket
from Models.Client import c_MQTTClient
from Models.FixHeader import c_FixHeader
from Models.VariableHeader import c_VariableHeader
from Models.Payload import c_Payload
from Models.FixHeaderFlags import c_FixHeaderFlags
from Models.ConnectHeader import c_ConnectHeader
from Models.ConnackHeader import c_ConnackHeader
from Models.ContentFlagByte import c_ContentFlagByte
from Models.SubackPayload import c_SubackPayload
from Models.SubscribePayload import c_SubscribePayload
from Models.ConnectPayload import c_ConnectPayload
from Models.UnsubscribePayload import c_UnSubscribePayload
from MQTTHelper import c_MQTTHelper
import codecs
class c_ClientManager:
    ClientList = list()
    Helper = c_MQTTHelper()

    def GenerateUser(self,packet):
        command = self.Helper.GetCommand(packet)
        if command == "Connect":
            self.ClientList.append(self.GenereateConnectUser(packet))
            

        self.ClientList.append(c_MQTTClient(c_MQTTPacket(
            c_FixHeader(NULL,c_FixHeaderFlags(),NULL),
            c_VariableHeader(c_ConnectHeader(NULL,NULL,c_ContentFlagByte(NULL,NULL,NULL,NULL,NULL,NULL),NULL),c_ConnackHeader(NULL,NULL),),
            c_Payload(c_UnSubscribePayload(NULL),c_SubackPayload(NULL),c_SubscribePayload(NULL,NULL),c_ConnectPayload(NULL,NULL,NULL,NULL,NULL,NULL)))))    
    pass

    def GenereateConnectUser(self,packet):
        hexPacket = self.Helper.ConvertDecimalToHex(packet)
        PNlenght = self.GetProtocolNameLenght(int(hexPacket[2],16),int(hexPacket[3],16))
        fixheader = c_FixHeader(self.Helper.GetCommand(packet),c_FixHeaderFlags(NULL,NULL,NULL),int(hexPacket[1],16))
        varibleheader = c_VariableHeader(c_ConnectHeader(PNlenght,self.GetProtocolName(hexPacket,PNlenght),self.GetProtocolLeven(hexPacket,PNlenght),self.GetContentFlagByte(hexPacket,PNlenght + 5),int(hexPacket[PNlenght + 6],16) + int(hexPacket[PNlenght+ 7],16)),NULL,NULL,NULL)
        payload = c_Payload(NULL,NULL,NULL,self.GenerateConnectPayload(hexPacket,PNlenght+9,varibleheader))
        client = c_MQTTClient(c_MQTTPacket(fixheader,varibleheader,payload))
        return client


    def GenerateConnectPayload(self,packet,lenght,varibleheader):
        clientIdLenght = self.GetClientIdLenght(packet,lenght)
        clientId = self.GetClientId(packet,lenght+1,clientIdLenght)
        usernameLenght = self.GetUsernameLenght(packet,lenght+clientIdLenght+2,varibleheader)
        username = self.GetUsername(packet,lenght+3+clientIdLenght,usernameLenght)
        passwordLenght = self.GetPasswordLenght(packet,lenght+4+clientIdLenght+usernameLenght,varibleheader)
        password = self.GetPassword(packet,lenght+5+clientIdLenght+usernameLenght,passwordLenght)
        return c_ConnectPayload(clientIdLenght,clientId,usernameLenght,username,passwordLenght,password)


    def GetUsernameLenght(self,packet,lenght,varibleheader:c_VariableHeader):
        uLenght = 0
        if varibleheader._ConnectHeader._ContentFlagByte.UsernameFlag == True:
               uLenght = int(packet[lenght],16)
        return uLenght

    def GetUsername(self,packet,lenght,uNameLenght):    
        byte = []
        for x  in range(lenght ,uNameLenght+lenght):
            byte.append(int(packet[x],16))
        temp = bytes(byte).decode('utf-8')
        return temp
    
    def GetPassword(self,packet,lenght,pLenght):    
        byte = []
        for x  in range(lenght ,pLenght+lenght):
            byte.append(int(packet[x],16))
        temp = bytes(byte).decode('utf-8')
        return temp
    
    def GetPasswordLenght(self,packet,lenght,varibleheader:c_VariableHeader):
        pLenght = 0
        if varibleheader._ConnectHeader._ContentFlagByte.PasswordFlag == True:
               pLenght = int(packet[lenght],16)
        return pLenght
    
    def GetClientId(self,packet,lenght,clientIdLenght):
        byte = []
        for x  in range(lenght ,clientIdLenght+lenght):
            byte.append(int(packet[x],16))
        temp = bytes(byte).decode('utf-8')
        return temp

    def GetClientIdLenght(self,packet,lenght):
        return int(packet[lenght],16)

    def GetProtocolNameLenght(self,lenght1,lenght2):
        return lenght1 + lenght2

    #Loop through the packet from start of prtocolname and to the end of protocolname
    #Then return the full name as string
    def GetProtocolName(self,packet,lenght):
        byte = []
        for x  in range(1,lenght + 1):
            byte.append(int(packet[3 + x],16))
        temp = bytes(byte).decode('utf-8')
        return temp

    #Return the packet after the protocolname
    def GetProtocolLeven(self,packet,lenght):
        return packet[lenght + 4]
    

    #Checks through an arry of the bit values that are set in the will flags
    #Then generates an WillFlagsObj with the values that we return
    def GetContentFlagByte(self,packet,lenght):
        WillQoS = 0
        setFlags = self.Helper.LeftBitwiseCheckFlags(int(packet[lenght],16))
        print(setFlags)
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



