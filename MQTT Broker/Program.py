import sys, getopt
from Server import c_Server

try :
    for i in sys.argv :
        print(sys.argv[i], end = " ")

except :
    pass
# end try

def Main():

    if(len(sys.argv) > 1):
        server = c_Server(sys.argv[1])
    else:
        server = c_Server()
        

Main()

