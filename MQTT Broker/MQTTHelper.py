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
        elif hex == "0xC0":
            tempStr = "Ping"
        elif hex == "0xE0":
            tempStr = "Disconnect"
        return tempStr


