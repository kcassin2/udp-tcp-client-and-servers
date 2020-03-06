from socket import *
serverName= "127.0.0.1"
serverPort = 12000
#operating system i want a new socket and i want it to be associated with a tcp ip network and connect it to udp
clientSocket= socket(AF_INET, SOCK_DGRAM)

#standard python getting code from the user
msg = str.endcode(input("Input a lower case sentence: "))

#i want to send msg to this server (takes the ip and port num)
clientSocket.sendto(msg, (serverName, serverPort))

#returns message and who sent the message
retmsg, serverAddress = clientSocket.recvfrom(2048)

print(retmsg)

#os closes the socket 
clientSocket.close() 
