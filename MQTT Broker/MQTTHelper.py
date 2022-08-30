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
        return
    
    def StringBuilder(self,packet):
        tempString = ""
        for item in packet:
            tempString += item
        return tempString


