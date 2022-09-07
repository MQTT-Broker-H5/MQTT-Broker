from concurrent.futures import thread
from datetime import datetime
from MQTTService import c_MQTTService
from MQTTHelper import c_MQTTHelper
import socket
from _thread import *
from Models.Client import c_MQTTClient

class c_Server:
    host = '0.0.0.0'
    port = 8000
    ThreadCount = 0
    MQTTService = c_MQTTService()
    MQTTHelper = c_MQTTHelper()

    def __init__(self):
        self.start_server(self.host, self.port)

    def __init__(self, port : int):
        
        hostname = socket.gethostname()    
        self.host = socket.gethostbyname(hostname) 
        self.port = int(port)
        print("ip:" + str(self.host) +  "\nPort:" + str(self.port))

        self.start_server(self.host, self.port)

    def client_handler(self,connection: socket.socket):
        
      
        lastPacket = None
        clientID = None
        
        while True:
            try:

                data = connection.recv(2048)

                if data is None or data is b'':
                    connection.close()

                    
                    continue

                cmd = self.MQTTHelper.GetCommand(data)

                if lastPacket is None:
                    lastPacket = datetime.now()
                
                    

                if cmd == "Disconnect": 
                    pass
                   
                elif(cmd == 'Connect'):
                    if self.MQTTService.ValidateConnect(data, connection) != True:
                        self.disconnect(clientID)
                        continue #Kill thread
                    clientID = self.MQTTHelper.GetClientName(data)
                    self.AcceptConnection(clientID)


                elif cmd == "Wrong input":
                    self.disconnect(clientID)
                
                elif cmd == "Ping":
                    print("ping")
                    if self.CheckKeepAlive(lastPacket, clientID) is True:
                        self.SendHeartbeat(clientID)
                        lastPacket = datetime.now()
                        print('pong')
                        #lav et countdown
                    else:
                        self.CloseCon(clientID)
                        self.disconnect(clientID)
                        thread._python_exit               

            except:
                self.sendLastWill(clientID)
                return
            
    def CheckKeepAlive(self, lastPacketTime : datetime, clientID):
        keepalive = self.MQTTService.GetKeepAlive(clientID)
        if self.MQTTHelper.KeepAliveChecker(keepalive, lastPacketTime) is False :
            return False
        return True



    def accept_connections(self, ServerSocket):
        while True:
            Client, address = ServerSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.client_handler, (Client, ))
    
    def start_server(self, host, port):
    
        c = int(32)
        ServerSocket = socket.socket()
        try:
            ServerSocket.bind((host, port))
        except socket.error as e:
            print(str(e))
        print(f'Server is listing on the port {port}...')
        ServerSocket.listen()
    
        start_new_thread(self.accept_connections, (ServerSocket, ))
        
        while True:
            inp = input('')
            if inp == "count":
                 print(len(self.clients))


    def SendMessage(self, clientID, message):
        try:
            client = self.MQTTService.ClientManager.GetClientByID(clientID)
            client._socket.send(message)
        except:
            pass

    def CloseCon(self, clientID):
        client : c_MQTTClient = self.MQTTService.ClientManager.GetClientByID(clientID) 
        client._socket.close()

    def AcceptConnection(self,  ClientID):
        self.SendMessage(ClientID, b'\x20\x02\x00\x00')
       
    def SendHeartbeat(self, clientID):
        self.SendMessage(clientID, b'\xD0\x00')
        
    def disconnect(self, clientID):
        self.sendLastWill(clientID)
        

    def sendLastWill(self, clientID):
        lastWill, topic = self.MQTTService.GetLastWill(clientID)
        clients = self.MQTTService.ClientManager.GetClientByTopic(topic)
        for count, sel in enumerate(clients):
            mqttClient : c_MQTTClient = sel 
            if mqttClient._MQTTPacket._Payload._ConnectPayload._ClientID == clientID:
                continue
            else:
                pass

         

        