from ClientManager import c_ClientManager
from MQTTHelper import c_MQTTHelper
from Models.Client import c_MQTTClient
class c_MQTTService:
    MQTTHelper = c_MQTTHelper()
    ClientManager = c_ClientManager()
    
    def ValidateConnect(self,packet):
        self.ClientManager.GenerateClient(packet)
        clientID = self.MQTTHelper.GetClientName(packet)
        print(clientID)
        client = self.ClientManager.GetClientByID(clientID)
        print(c_MQTTClient(client)._MQTTPacket._Payload._ConnectPayload.ClientID)
        #connectPakcet = []
        #print("Inside validateConnect")
        #print(packet)
        #connectPakcet.append(self.GetCommand(hexArray[0]))
        #self.VlaidatePacketLenght(int(hexArray[1],16),len(hexArray) - 2)
        #self.ValidateVaribleHeader(hexArray)
        pass
    
    def ValidateVaribleHeader(self,packet):
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
    
    # Incase of false return, disconnect client form the broker
    def ValidateProtocolName(self,lenght,packet):
        if lenght != len(packet):
            return False
        return True

    # Incase of false return, disconnect client form the broker
    def ValidateProtocolLeven(self,level):
        if level != "0x4":
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

