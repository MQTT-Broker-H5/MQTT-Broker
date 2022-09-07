import binascii
import os
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
    def GenereateConnectClient(self,packet, socket):
        self.hexPacket = self.Helper.ConvertDecimalToHex(packet)
        fixheader = c_FixHeader(self.Helper.GetCommand(packet),c_FixHeaderFlags(None,None,None),int(self.hexPacket[1],16))
        self.hexPacket = self.Helper.RemoveFromPacket(self.hexPacket,2)
        PNlenght = self.CombindInt(self.hexPacket,2)
        varibleheader = c_VariableHeader(c_ConnectHeader(PNlenght,self.GetString(self.hexPacket,PNlenght),self.GetLenght(self.hexPacket[0]),self.GetContentFlagByte(self.hexPacket),self.CombindInt(self.hexPacket,2)),None,None,None)
        payload = c_Payload(None,None,None,self.GenerateConnectPayload(self.hexPacket,varibleheader))
        client = c_MQTTClient(c_MQTTPacket(fixheader,varibleheader,payload), socket)
        return client

    #Generats the payload for the connect client
    #Mapps it and returns c_ConnectPayload obj
    def GenerateConnectPayload(self,packet,varibleheader:c_VariableHeader):
        clientIdLenght = self.CombindInt(packet,2)

        if clientIdLenght == 0:
            clientId = self.GenerateUniqClientID()
        else:
            clientId = self.GetString(packet,clientIdLenght)

        usernameLenght = 0
        passwordLenght = 0
        username = ""
        password = ""

        if varibleheader._ConnectHeader._ContentFlagByte._WillFlag == True:
            willTopicLenght = self.CombindInt(packet,2)
            willTopic = self.GetString(packet,willTopicLenght)
            willMessageLenght = self.CombindInt(packet,2)
            willMessage = self.GetString(packet,willMessageLenght)
        if varibleheader._ConnectHeader._ContentFlagByte._UsernameFlag == True:
            usernameLenght = self.CombindInt(packet,2)
            username = self.GetString(packet,usernameLenght)
        if varibleheader._ConnectHeader._ContentFlagByte._PassworFlag == True:
            passwordLenght = self.CombindInt(packet,2)
            password = self.GetString(packet,passwordLenght)
        return c_ConnectPayload(clientIdLenght,clientId,willTopicLenght,willTopic,willMessageLenght,willMessage,usernameLenght,username,passwordLenght,password)

    #Generates a uniq clientID if none is presented in the payload
    def GenerateUniqClientID(self):
        clientID = "MQTT_" + str(binascii.hexlify(os.urandom(8)).decode('utf-8'))
        return clientID


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
        self.Helper.RemoveFromPacket(self.hexPacket,None)
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
        self.Helper.RemoveFromPacket(self.hexPacket,None)
        if setFlags[1] == 1:
            CleanSession = True
        elif setFlags[1] != 1:
            CleanSession = False
        if setFlags[2] == 1:
            Willflag = True
        elif setFlags[2] != 1:
            Willflag = False
            setFlags[3] = 0
            setFlags[4] = 0
            setFlags[5] = 0
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
            UsernameFlag = True
        elif setFlags[6] != 1:
            UsernameFlag = False
            setFlags[7] = 0
        if setFlags[7] == 1:
            PasswordFlag = True
        elif setFlags[7] != 1:
            PasswordFlag = False
        return c_ContentFlagByte(CleanSession,Willflag,WillQoS,WillRetain,PasswordFlag,UsernameFlag)