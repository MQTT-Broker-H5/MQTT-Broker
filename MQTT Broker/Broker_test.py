from array import array
from asyncio.windows_events import NULL
from contextlib import nullcontext
from ClientManager import c_ClientManager
from MQTTHelper import c_MQTTHelper
from MQTTService import c_MQTTService
import unittest

class Broker_test(unittest.TestCase):
    
    connect = b'\x10\x1a\x00\x04MQTT\x04\x02\x00\n\x00\x0emqttx_69d85a39'
    clientManager = c_ClientManager()
    mService = c_MQTTService()

    def test_CreatePackage(self) :
   
       result = self.clientManager.GetUsers()
       amount = len(result)
       self.assertIs(amount, 0, "Contains 0")

    def test_AddUser(self) :
        self.mService.ClientManager.GenerateUser(self.connect)
        amount = len(self.mService.ClientManager.ClientList)
        self.assertIs(amount, 1, "contains 1")

    def test_GetUserByID(self) : 
        user = self.mService.ClientManager.GetUserbyID('mqttx_69d85a39')
        self.assertIsNot(user, NULL, "user found")

    def test_GenerateUser (self):
        user = self.mService.ClientManager.GenerateUser(self.connect)
        self.assertIsNot(user, NULL, "Removed user from list")

    def test_DecimalToToHex(self):
        hex = self.clientManager.Helper.ConvertDecimalToHex(self.connect)
        print(str(hex))
        self.assertIsNot(hex, "", "Converted: " + str(hex))

    def test_HexToDecimal(self):
        utf = self.clientManager.Helper.ConvertHexToDecimal(self.connect)    
        print(utf)
        self.assertIsNotNone(utf)

    def test_GetConnectCommand(self):
       con = self.clientManager.Helper.GetCommand(self.connect)
       self.assertIs(con, "Connect")

    def test_GetConnackCommand(self):
        con = self.clientManager.Helper.GetCommand(b'\x20\x02\x00\x00')
        self.assertIs(con, "Connack")