from ClientManager import c_ClientManager
from MQTTHelper import c_MQTTHelper
from Models.Client import c_MQTTClient
class c_MQTTService:
    MQTTHelper = c_MQTTHelper()
    ClientManager = c_ClientManager()
    
    def ValidateConnect(self,packet):
        self.ClientManager.GenerateClient(packet)
        clientID = self.MQTTHelper.GetClientName(packet)
        client = self.ClientManager.GetClientByID(clientID)
        if self.ValidateVariableHeader(client) != True:
            return False

        return True

    def ValidateVariableHeader(self, client:c_MQTTClient):
        print("In validate header")
        if self.ValidateProtocolName(client) != True:
            return False
        if self.ValidateProtocolLeven(client) != True:
            return False
        if self.ValidateFlags(client) != True:
            return False


        pass

    def ValidateProtocolName(self,client:c_MQTTClient):
        print("In validate protocol name")
        lenght = client._MQTTPacket._VaribleHeader._ConnectHeader.ProtocolNameLenght
        name = client._MQTTPacket._VaribleHeader._ConnectHeader.ProtocolName

        if len(name) != lenght:
            return False
        return True

    def ValidateProtocolLeven(self,client:c_MQTTClient):
        if client._MQTTPacket._VaribleHeader._ConnectHeader.ProtocolLevel != 4:
            return False
        return True

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
        if flags.Willflag == True:
            if


        pass
    
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

    def ValidateFlag(self,byte,flags):
        temp = [False,False,False,False,False,False,False,False]
        QoS = []
        for bit in byte:
            if bit == 1:
                temp[0] = True
                #Disconnect
                pass
            elif bit ==2:
                temp[1] = True
                #Discard old session if exist, and start new
                pass
            elif bit ==3:
                temp[2] = True
                #Store will message
                pass
            elif bit ==4:
                QoS.append(bit)
                pass
            elif bit ==5:
                QoS.append(bit)
                pass
            elif bit ==6:
                temp[5] = True
                #Store will message as a retained message
                pass
            elif bit ==7:
                temp[6] = True
                #Check for username in payload
                pass
            elif bit ==8:
                temp[7] = True
                #Cheack for Password in payload
                pass
        for index in temp:
            if temp[index] == False:
                pass


        if len(QoS) == 2:
            #Disconnect
            pass
        elif len(QoS) != 2:
            print("QoS: " + self.GenerateQoS())
            pass


    def GenerateQoS(self,QoS):
        qos = 3
        if len(QoS) != 0:
            if QoS[0] != 4:
                qos = 2
            elif QoS[0] == 4:
                qos = 1
        return qos

        
    def ResumeConnection(self,):
        pass
    #Return True if the first bit in the byte is set.
    #We are using bitwise operator left shifting to check if the bit is set
    def ReservedBitInFlags(self,flags):
        reservedBit = 1
        if flags & (1 << (reservedBit -1)):
            return True
        return False
    
    #Return True if the secound bit in the byte is set
    def CleanSessionBitInFlags(self,flags):
        print(flags)
        cleanSessionBit = 2
        if flags & (1 << (cleanSessionBit -1)):
            return True
        return False

