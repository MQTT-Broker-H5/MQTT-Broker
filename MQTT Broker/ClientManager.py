from asyncio.windows_events import NULL
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
class c_ClientManager:
    ClientList = list()

    def GenerateUser(self,packet):
        self.ClientList.append(c_MQTTClient(c_MQTTPacket(
            c_FixHeader(NULL,c_FixHeaderFlags(),NULL),
            c_VariableHeader(c_ConnectHeader(NULL,NULL,c_ContentFlagByte(NULL,NULL,NULL,NULL,NULL,NULL),NULL),c_ConnackHeader(NULL,NULL),),
            c_Payload(c_UnSubscribePayload(NULL),c_SubackPayload(NULL),c_SubscribePayload(NULL,NULL),c_ConnectPayload(NULL,NULL,NULL,NULL,NULL,NULL)))))    
    pass




