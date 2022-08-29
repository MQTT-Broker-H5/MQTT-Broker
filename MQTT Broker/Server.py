from ast import For, Str

import socket
from _thread import *
from stringprep import c22_specials
from time import process_time_ns
from tkinter import Y
from wsgiref import validate
from xml.etree.ElementTree import tostring
class Server:
    host = '127.0.0.1'
    port = 8000
    ThreadCount = 0
    clients = list()

    def __init__(self):
        self.start_server(self.host, self.port)

    def client_handler(self,connection):
        self.clients.append(connection)
        connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
        while True:
            try:
                data = connection.recv(2048)
                print("Data under:")
                print(data)
                print("end of data")
                message = data.decode('utf-8')
                print(self.SplitString(message))

                if message == 'BYE':
                    break
                reply = f'Server: {message}'
                connection.sendall(str.encode(reply))
            except :
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

    @staticmethod
    def SplitString(message):
        print(len(message))
        for x in range(len(message)):
            print(x)
        temp = message
        return temp





