from asyncio.windows_events import NULL
from ConnectMapper import c_ConnectMapper
from MQTTHelper import c_MQTTHelper
class c_ClientManager:
    ClientList = list()
    Helper = c_MQTTHelper()
    cMapper = c_ConnectMapper()

    
    #Metode der returnere en liste af c_MQTTClient
    #map will topic

    def GenerateUser(self,packet):
        command = self.Helper.GetCommand(packet)
        if command == "Connect":
            self.ClientList.append(self.cMapper.GenereateConnectUser(packet))

    pass


