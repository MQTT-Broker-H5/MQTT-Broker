from base64 import decode, encode
from codecs import utf_7_encode
from http import client
from itertools import tee
from pydoc import cli
from queue import PriorityQueue
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
    helper = c_MQTTHelper()
    def __init__(self):
        self.start_server(self.host, self.port)

    def client_handler(self,connection):
        self.clients.append(connection)
        # connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
        while True:
            try:
               
             
              
                
                data = connection.recv(2048)
               
                # connection.sendall(data)

                print(b'\x20\x02\x00\x00')
                print(type(b'\0x20\0x02\0x00\0x00'))
                connection.sendall(b'\x20\x02\x00\x00')
                
                # print("Data under:")
                # print(data)
                # print("end of data")
                # # self.MQTTService.ValidateConnect(data)
                # hexarray = self.helper.ConvertDecimalToHex(data)
                # #utf form
            
                # message = data.decode('utf-8')
                
                # print()
                # # teem =  self.MQTTService.
                # (hexarray[0])
                 
                # teem2 = "\0x20\0x02\0x00\0x00\0x00"
            
                # if message == 'BYE':
                #     break
                # reply = f'Server: {message}'
                # connection.sendall(str.encode(teem2))
            except error as err:
                print(err)
                # connection.close()
                # connection.close()
            

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





