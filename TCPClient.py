from socket import *

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
#for tcp we do a connect, it creates a stream, creates connection between client and server
clientSocket.connect((serverName, serverPort))

msg = str.encode(input("Input a lower case sentence: "))

#sending message and waiting to see what we get back
clientSocket.send(msg)

newmsg = clientSocket.recv(1024)

print("From the server")
print(newmsg)

clientSocket.close()


