from operator import truediv
from sqlite3 import connect
from ClientManager import c_ClientManager
from MQTTHelper import c_MQTTHelper
class c_MQTTService:
    MQTTHelper = c_MQTTHelper()
    ClientManager = c_ClientManager()
    
    
    def ValidateConnect(self,packet):
        connectPakcet = []
        print("Inside validateConnect")
        print(packet)
        hexArray = self.MQTTHelper.ConvertDecimalToHex(packet)
        connectPakcet.append(self.GetCommand(hexArray[0]))
        self.VlaidatePacketLenght(int(hexArray[1],16),len(hexArray) - 2)
        self.ValidateVaribleHeader(hexArray)
        pass
    
    def ValidateVaribleHeader(self,packet):
        PNPacket = []
        PNLenght = int(packet[2],16)+ int(packet[3],16)
        for x  in range(1,PNLenght + 1):
            PNPacket.append(packet[3 + x])
        self.ValidateProtocolName(PNLenght,PNPacket)
        self.ValidateProtocolLeven(packet[8])
        self.LeftBitwiseCheckFlags(int(packet[9],16))
        #self.ReservedBitInFlags(int(packet[9],16))
        #print(self.CleanSessionBitInFlags(int(packet[9],16)))
        pass

    #Incase of default value, disconnect client from the broker
    def GetCommand(self,hex):
        tempStr = "Wrong input"
        if hex == "0x10":
            tempStr = "Connect"
        elif hex == "0x30":
            tempStr = "Publish"
        elif hex == "0x80":
            tempStr = "Subscribe"
        elif hex == "0xC0":
            tempStr = "Ping"
        elif hex == "0xE0":
            tempStr = "Disconnect" 
        return tempStr

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

    #We are using bitwise operator left shifting to check if the bit is set
    #If the bit is set we add it to an arry so we can do validation them
    def LeftBitwiseCheckFlags(self,flags):
        reservedBits = []
        for kth in range(1,9):
            if flags &(1 << (kth -1)):
                reservedBits.append(kth)
        return reservedBits


    def ValidateFlag(self,byte,flags):
        QoS = []
        for bit in byte:
            if bit == 1:
                #Disconnect
                pass
            elif bit ==2:
                pass
            elif bit ==3:
                #Store will message
                pass
            elif bit ==4:
                QoS.append(bit)
                pass
            elif bit ==5:
                QoS.append(bit)
                pass
            elif bit ==6:
                #Store will message as a retained message
                pass
            elif bit ==7:
                #Check for username in payload
                pass
            elif bit ==8:
                #Cheack for Password in payload
                pass

        if len(QoS) == 2:
            #Disconnect
            pass
        elif len(QoS) != 2:
            #Generate QoS Method
            pass


    def GenerateQoS()
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

