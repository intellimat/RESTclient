import json
import socket

####################    Methods' definitions    ####################
def connectTo(IP, PORT): #tries to reach a server running on IP and PORT specified
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    return s

def readResponse(socket): #reads the message coming from the client
    rawData = socket.recv(8192)
    decodedData = rawData.decode("utf-8")
    return decodedData

def closeConnection(socket): #closes a TCP connection reachable through the socket argument
    host, port = socket.getpeername()
    socket.close()
    print(f'\nThe connection to {host} on port {port} has been closed by the server')

def writeGETrequest(s):
    host, port = socket.getpeername()
    socket.send(bytes(s,"utf-8"))

def getJSONobjectFromString(s):
    return json.loads(s)

def getBodyFromHTTPresponse(serverResponse):
    body = serverResponse.split('\r\n\r\n')[1]
    return body

####################    Here the execution starts    ####################
try:
    connectTo('www.sigua.ua.es', 80)
except socket.error as e:
    print('The client could not established a connection to the web server.\n')
