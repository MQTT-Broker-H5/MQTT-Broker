from asyncio.windows_events import NULL
from http import client
from multiprocessing.connection import Client
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
        fixheader = c_FixHeader(self.Helper.GetCommand(packet),c_FixHeaderFlags(NULL,NULL,NULL),int(hexPacket[1],16))
        varibleheader = c_VariableHeader(c_ConnectHeader(int(hexPacket[2],16)+ int(hexPacket[3],16),self.GetProtocolName(hexPacket),))
        payload = c_Payload()

        client = c_MQTTClient(c_MQTTPacket(fixheader,varibleheader,payload))
        return client

    def GetProtocolName(self,packet):
        byte = []
        for x  in range(1,int(packet[2],16) + int(packet[3],16) + 1):
            byte.append(int(packet[3 + x],16))
        temp = bytes(byte).decode('utf-8')
        return temp



