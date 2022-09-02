from asyncio.windows_events import NULL
from concurrent.futures import thread
from contextlib import nullcontext
from http import client
from pydoc import cli
from re import X
from socketserver import DatagramRequestHandler
from sqlite3 import connect
from MQTTService import c_MQTTService
from MQTTHelper import c_MQTTHelper
import socket
from _thread import *
class c_Server:
    host = '127.0.0.1'
    port = 8000
    ThreadCount = 0
    clients = list()
    MQTTService = c_MQTTService()
    MQTTHelper = c_MQTTHelper()

    def __init__(self):
        self.start_server(self.host, self.port)

    def client_handler(self,connection: socket.socket):
        
        self.clients.append(connection)
        while True:
            try:
                data = connection.recv(2048)

                if not data:
                    self.disconnect(connection)
                    self.clients.remove(connection)
                    

                cmd = self.MQTTHelper.GetCommand(data)

                if cmd == "Disconnect": 
                    self.clients.remove(connection)
                   
                elif(cmd == 'Connect' and  connection in self.clients):
                    self.MQTTService.ValidateConnect(data)
                    #self.AcceptConnection(connection)

                elif cmd == "Wrong input":
                    self.disconnect(connection)
                
                elif cmd == "Ping":
                    self.SendHeartbeat(connection)
               

            except:
                connection.close()
            

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



    def AcceptConnection(self,  clientCon : socket.socket):
       clientCon.send(b'\x20\x02\x00\x00')
       
    def SendHeartbeat(self, clientCon : socket.socket):
            clientCon.send(b'\xD0\x00')
        
    def disconnect(self,  clientCon: socket.socket):
        clientCon.close()
        self.clients.remove(clientCon)

    def sendLastWill(self, client : socket.socket):
         for count, sel in enumerate(self.clients) :
            if(sel == client):
                continue
            else:
                sel : socket.socket
                sel.send('')