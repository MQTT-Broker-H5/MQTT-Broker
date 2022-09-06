from asyncio.windows_events import NULL
from ConnectMapper import c_ConnectMapper
from MQTTHelper import c_MQTTHelper
from Models.Client import c_MQTTClient
from _thread import *
class c_ClientManager:
    ClientList = list()
    Helper = c_MQTTHelper()
    cMapper = c_ConnectMapper()

    #Creats a new client based on the packet
    #Add it to the clientlist
    def GenerateClient(self,packet):
        command = self.Helper.GetCommand(packet)
        if command == "Connect":
            self.ClientList.append(self.cMapper.GenereateConnectClient(packet))

    #Get a specifik client from the clientList
    def GetClientByID(self, clientID):
        for i in range(len(self.ClientList)):
            if self.ClientList[i]._MQTTPacket._Payload._ConnectPayload._ClientID == clientID:
                return self.ClientList[i]
        else:
            return "No match"
                

