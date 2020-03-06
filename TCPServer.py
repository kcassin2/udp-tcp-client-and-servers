from socket import*

serverPort= 12000
serverSocket = socket( AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))


#listen means you're sitting there waiting for somthing to connect (in udp u just get a package and you're good to go)

serverSocket.listen(1)
print("The server is ready")

#once we have a connection we have a server socket accept 
while 1:
    connectionSocket, addr = serverSocket.accept()

    msg= connectionSocket.recv(1024)
    newmsg= msg.upper()
    connectionSocket.send(newmsg)
    connectionSocket.close()
    
    
