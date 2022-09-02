from asyncio.windows_events import NULL
from multiprocessing.connection import Client
from ConnectMapper import c_ConnectMapper
from MQTTHelper import c_MQTTHelper
from Models.Client import c_MQTTClient
from asyncio.windows_events import NULL

class c_ClientManager:
    ClientList = list() 
    Helper = c_MQTTHelper()
    cMapper = c_ConnectMapper()

    
    #Metode der returnere en liste af c_MQTTClient
    #map will topic

    def GenerateUser(self,packet):
        command = self.Helper.GetCommand(packet)
        if command == "Connect":
            self.ClientList.append(self.cMapper.GenereateConnectUser(packet))

    pass

    def GetUser(self):
        return self.ClientList
    
    def GetUserbyID(self, clientID : str) :
        for x in self.ClientList :  
            c = (c_MQTTClient(self.ClientList[x]))._MQTTPacket._Payload._ConnectPayload.ClientID
            if( c == clientID) :
                return c 

