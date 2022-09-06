from ClientManager import c_ClientManager
from MQTTHelper import c_MQTTHelper
from Models.Client import c_MQTTClient
class c_MQTTService:
    MQTTHelper = c_MQTTHelper()
    ClientManager = c_ClientManager()
    
    #Validates the connectPacket that we get on connect
    def ValidateConnect(self,packet):
        self.ClientManager.GenerateClient(packet)
        clientID = self.MQTTHelper.GetClientName(packet)
        client = self.ClientManager.GetClientByID(clientID)
        if self.ValidateVariableHeader(client) != True:
            return False

        return True

    #Validates the varibleheader from the connect packet
    #This method only works with connect packet
    def ValidateVariableHeader(self, client:c_MQTTClient):
        print("In validate header")
        if self.ValidateProtocolName(client) != True:
            return False
        if self.ValidateProtocolLeven(client) != True:
            return False
        if self.ValidateFlags(client) != True:
            return False
        return True

    #Validates the protocolname
    def ValidateProtocolName(self,client:c_MQTTClient):
        print("In validate protocol name")
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
        if flags.CleanSession == False:
            #Do not remove the client session if the client disconnect
            #If the cleansSession is 0
            print("worked")
        elif flags.CleanSession == True:
            #Discard old session and start a new session
            #Do not save data in case of reconnect
            print("worked")
        return True
