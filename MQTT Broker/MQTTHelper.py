from asyncio.windows_events import NULL
from contextlib import nullcontext
from struct import pack
class c_MQTTHelper:
    def ConvertHexToUtf(self,packet):
        return
    
    def ConvertHexToDecimal(self,packet):
        decimalPacket = []
        for data in packet:
            decimalPacket.append(data)
        return decimalPacket

    def ConvertUtfToDeciaml(self,packet):
        return

    def ConvertDecimalToHex(self,packet):
        hexPacket = []
        for data in packet:
            hexPacket.append(hex(data))
        return hexPacket

    def ConvertDecimalToUtf(self,packet):
        return

    def ConvertUtfToHex(self,packet):
        print("MQTTHelper: " + packet)
        hexPacket = []
        for i, data in enumerate(packet):
            hexPacket.append(data)
        print("string builder: " + c_MQTTHelper.StringBuilder(self,hexPacket))
        print(hexPacket)
        return hexPacket
    
    def StringBuilder(self,packet):
        tempString = ""
        for item in packet:
            tempString += item
        return tempString
    
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
        elif hex == "0x20":
            return "Connack"
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
                try:
                    packet.pop(i)
                except: 
                    continue
        else:
            try:
                packet.pop(0)
            except :
                return NULL
        return packet


