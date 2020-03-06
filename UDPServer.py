from socket import*

serverPort =12000

#create socket server
serverSocket= socket( AF_INET, SOCK_DGRAM)

#you have to bind server to listen to socket for connections (its on ip address and listening to server)
serverSocket.bind(('', serverPort))

print("OK the server is read")

#
while 1:
    msg, clientAddress = serverSocket.revfrom(2048)
    newmsg = msg.upper()
    serverSocket.sendto(newmsg, clientAddress)
