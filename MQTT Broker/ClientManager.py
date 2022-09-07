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
    def GenerateClient(self,packet, socket):
        command = self.Helper.GetCommand(packet)
        if command == "Connect":
            self.ClientList.append(self.cMapper.GenereateConnectClient(packet, socket))

    #Get a specifik client from the clientList
    def GetClientByID(self, clientID):
        for i in range(len(self.ClientList)):
            if self.ClientList[i]._MQTTPacket._Payload._ConnectPayload._ClientID == clientID:
                return self.ClientList[i]
        else:
            return "No match"

    def GetClientByTopic(self, topic):
        clients = []
        for i in range(len(self.ClientList)):
            try:
                if self.ClientList[i]._MQTTPacket._Payload._ConnectPayload._WillTopic == topic:
                    clients.append(self.ClientList[i])
            except:
                continue
        return clients
        

    def RemoveClient(self, clientId) :
        try:
            for i in range(len(self.ClientList)):
                if self.ClientList[i]._MQTTPacket._Payload._ConnectPayload._ClientID == clientId:
                    self.ClientList.pop(i)
                    return True
        except:
            return False

                

    def GetUsers(self):
        return self.ClientList

