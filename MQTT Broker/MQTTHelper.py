from asyncio.windows_events import NULL
from struct import pack
class c_MQTTHelper:

    #Converts string hex format to decimal
    def ConvertHexToDecimal(self,packet):
        decimalPacket = []
        for data in packet:
            decimalPacket.append(data)
        return decimalPacket

    #Converts Decimal packet to string in hex format
    def ConvertDecimalToHex(self,packet):
        hexPacket = []
        for data in packet:
            hexPacket.append(hex(data))
        return hexPacket

    #Incase of default value, disconnect client from the broker
    def GetCommand(self,packet):
        hex = self.ConvertDecimalToHex(packet)[0]
        tempStr = "Wrong input"
        if hex == "0x10":
            tempStr = "Connect"
        elif hex == "0x30":
            tempStr = "Publish"
        elif hex == "0x80":
            tempStr = "Subscribe"
        elif hex == "0xc0":
            tempStr = "Ping"
        elif hex == "0xe0":
            tempStr = "Disconnect"
        elif hex == "xc0":
            tempStr = "Heartbeat"
        elif hex == "x02":
            tempStr = "Ping"
        return tempStr

    #We are using bitwise operator left shifting to check if the bit is set
    #If the bit is set we add it to an arry so we can do validation them
    def LeftBitwiseCheckFlags(self,flags):
        reservedBits = []
        for kth in range(1,9):
            if flags &(1 << (kth -1)):
                reservedBits.append(1)
            else:
                reservedBits.append(0)
        return reservedBits

    #Insert the ammount you wanted to be removed from the list
    #The remove will happel from 0-ammount
    #If you just want 1 item removed insert null in ammount
    def RemoveFromPacket(self,packet:list,ammount):
        if ammount != NULL:
            for i in range(0, ammount):
                i = 0
                packet.pop(i)
        else:
            packet.pop(0)
        return packet
    
    #Get the lenght of the packet
    #Lenght determens how much of the packet u want from start pos of the packet
    def GetLenght(self,packet,lenght):
        newLenght = 0
        for i in range(1,lenght):
            newLenght += int(packet[i],16)
        return newLenght

    #Get the client name of a packet in string format
    def GetClientName(self,packet):
        clientID = ""
        command = self.GetCommand(packet)
        hexPacket = self.ConvertDecimalToHex(packet)
        identifyer = 0
        clientIdLenght = 0
        if command == "Connect":
            self.RemoveFromPacket(hexPacket,2)
            PNLenght = self.GetLenght(hexPacket,2)
            print(PNLenght)
            identifyer = PNLenght + 6
            self.RemoveFromPacket(hexPacket,identifyer)
            clientIdLenght = self.GetLenght(hexPacket,2)
            self.RemoveFromPacket(hexPacket,2)
            clientID = self.GetClientId(hexPacket,clientIdLenght)
            
        return clientID

    #Gets the client id from the packet and returns it in a string array
    def GetClientId(self,packet,lenght):
        byte = []
        for x  in range(lenght):
            byte.append(int(packet[x],16))
        temp = bytes(byte).decode('utf-8')
        return temp

