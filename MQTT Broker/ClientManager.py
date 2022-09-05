from asyncio.windows_events import NULL
from distutils.log import error
from ConnectMapper import c_ConnectMapper
from MQTTHelper import c_MQTTHelper
from Models.Client import c_MQTTClient
class c_ClientManager:
    ClientList = list()
    Helper = c_MQTTHelper()
    cMapper = c_ConnectMapper()

    #Creats a new client based on the packet
    #Add it to the clientlist
    def GenerateClient(self,packet):
        client:c_MQTTClient
        command = self.Helper.GetCommand(packet)
        if command == "Connect":
            self.ClientList.append(self.cMapper.GenereateConnectClient(packet))

    #Get a specifik client from the clientList
    def GetClientByID(self, clientID):
        try:
            print("In get client by id")
            print(len(self.ClientList))
            x = c_MQTTClient(self.ClientList[0])
            y = x._MQTTPacket
            h = y._Payload
            v = h._ConnectPayload
            t = v.ClientID
            print(t)
            for x in range(0,len(self.ClientList)):
                c = (c_MQTTClient(self.ClientList[x]))._MQTTPacket._Payload._ConnectPayload.ClientID
        except error as er:
            print(er)


