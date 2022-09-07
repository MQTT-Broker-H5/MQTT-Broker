from ClientManager import c_ClientManager
from MQTTHelper import c_MQTTHelper
from Models.Client import c_MQTTClient

class c_MQTTService:
    MQTTHelper = c_MQTTHelper()
    ClientManager = c_ClientManager()
    

    #Validates the connectPacket that we get on connect
    def ValidateConnect(self,packet, socket):
        self.ClientManager.GenerateClient(packet, socket)
        clientID = self.MQTTHelper.GetClientName(packet)
        client = self.ClientManager.GetClientByID(clientID)
        #if self.ValidateVariableHeader(client) != True:
            #return False

        return True

    #Validates the varibleheader from the connect packet
    #This method only works with connect packet
    def ValidateVariableHeader(self, client:c_MQTTClient):
        if self.ValidateProtocolName(client) != True:
            return False
        if self.ValidateProtocolLeven(client) != True:
            return False
        if self.ValidateFlags(client) != True:
            return False
        return True

    def GetLastWill(self, clientID):
        client : c_MQTTClient = self.ClientManager.GetClientByID(clientID)
        message = client._MQTTPacket._Payload._ConnectPayload._WillMessage
        topic = client._MQTTPacket._Payload._ConnectPayload._WillTopic
        return message, topic

    def ValidateProtocolName(self,client:c_MQTTClient):
        lenght = client._MQTTPacket._VaribleHeader._ConnectHeader._ProtocolNameLenght
        name = client._MQTTPacket._VaribleHeader._ConnectHeader._ProtocolName

        if len(name) != lenght:
            return False
        return True

    #Validates the protocol level
    def ValidateProtocolLeven(self,client:c_MQTTClient):
        if client._MQTTPacket._VaribleHeader._ConnectHeader._ProtocolLevel != 4:
            return False
        return True

    #Validates the connection flags
    def ValidateFlags(self,client:c_MQTTClient):
        flags = client._MQTTPacket._VaribleHeader._ConnectHeader._ContentFlagByte
        if flags._CleanSession == False:
             
            #Do not remove the client session if the client disconnect
            #If the cleansSession is 0
            print("worked")
        elif flags._CleanSession == True:
            #Discard old session and start a new session
            #Do not save data in case of reconnect
            print("worked")


    def GetKeepAlive(self, ClientID):
        try:
            client: c_MQTTClient = self.ClientManager.GetClientByID(ClientID)
            keepalive = client._MQTTPacket._VaribleHeader._ConnectHeader._KeepAlive
            return keepalive
        except :
            return -1
    
    
    def GetClientByPacket(self, packet):
        try:
            id = self.MQTTHelper.GetClientName(packet)
            return self.ClientManager.GetClientByID(id) 
        except:
            return None

    def DiscardClient(self, clientID):
        try:
            client : c_MQTTClient = self.ClientManager.GetClientByID(clientID)
            
            flags = client._MQTTPacket._VaribleHeader._ConnectHeader._ContentFlagByte
            if flags._CleanSession == True :
                if(self.ClientManager.RemoveClient(client._MQTTPacket._Payload._ConnectPayload._ClientID) is True):
                    return True
        except:
            return False
          
        
    

    def ValidateVaribleHeader2(self,packet):
        PNPacket = []
        PNLenght = int(packet[2],16)+ int(packet[3],16)
        for x  in range(1,PNLenght + 1):
            PNPacket.append(packet[3 + x])
        self.ValidateProtocolName(PNLenght,PNPacket)
        self.ValidateProtocolLeven(packet[8])
        #self.ReservedBitInFlags(int(packet[9],16))
        #print(self.CleanSessionBitInFlags(int(packet[9],16)))
        pass

    # Incase of false return, disconnect client form the broker
    def VlaidatePacketLenght(self,contentLenght,packetLenght):
        if contentLenght != packetLenght:
            return False
        return True
