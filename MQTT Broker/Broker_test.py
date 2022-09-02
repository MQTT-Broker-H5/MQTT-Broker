from array import array
from asyncio.windows_events import NULL
from ClientManager import c_ClientManager
import unittest

class Broker_test(unittest.TestCase):
    

    def test_CreatePackage(self) :
       clientManager = c_ClientManager()
       result = clientManager.GetUsers()
       amount = len(result)
       self.assertIs(amount, 0, "Contains 0")

    def test_add(self) :
        
        pass
