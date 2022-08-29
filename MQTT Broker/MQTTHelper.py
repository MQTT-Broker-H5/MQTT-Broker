from ast import literal_eval
from struct import pack
from unicodedata import decimal
from xml.dom.minidom import Element
class MQTTHelper:
    def ConvertHexToUtf(self,packet):
        utfPacket = []
        for data in packet:
            utfPacket.append(hex(data))
        return utfPacket
    
    @staticmethod
    def ConvertHexToDecimal(self,packet):
        decimalPacket = []
        for data in packet:
            decimalPacket.append(data)
        return decimalPacket

    def ConvertUtfToDeciaml(self,packet):
        return

    @staticmethod
    def ConvertDecimalToHex(self,packet):
        hexPacket = []
        print(packet)
        for data in packet:
            hexPacket.append(hex(data))
        print(hexPacket)
        return
    def ConvertDecimalToUtf(self,packet):
        return

    @staticmethod
    def ConvertUtfToHex(self,packet):
        print("MQTTHelper: " + packet)
        hexPacket = []
        for i, data in enumerate(packet):
            hexPacket.append(data)
        print("string builder: " + MQTTHelper.StringBuilder(self,hexPacket))
        print(hexPacket)
        return
    

    @staticmethod
    def StringBuilder(self,packet):
        tempString = ""
        for item in packet:
            tempString += item
        return tempString


