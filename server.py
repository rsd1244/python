#!/user/bin/env python

import socket

#Setup variables for the sockets
TCP_IP = "<Machine's IP ADDRESS or loopback>"
TCP_PORT = "<Port>"
#How big you want the messages you receive, it is buffer overflow resistant
BUFFER_SIZE = <Number>

#Basic socket required to setup in python
s = socket.socket)socket.AF_INET, socket.SOCK_STREAM)

#Asking the OS for permission to use the combinitation of port/socket
s.bind((TCP_IP, TCP_PORT))
#This can be rejected if the port was used recently

#Sets up the socket to listen on
s.listen()

#Storing the conn and addr parts of a socket, IFF the socket was bound
conn, addr = s.accept()

#Looping to make sure the program does not end after a single input
while True:
 #The buffer of received information
 data = conn.recv(BUFFER_SIZE)
 
 #If the data is empty, move on
 if not data: break
 
 #Displays the Client's current IP address and port used to send the message
 print ("Message Origin is: ", addr)

 #Prints too much information for me personally
 print ("Connection Info: ", conn)

 #Shows the data to the user on the server to give show what was sent
 print ("Received data: ", data.decode('utf-8'))

 #This is the return message sent to the client
 Reply = "You sent: " + data.decided('utf-8')
 #Sending the message back through to give the client feedback using conn that was opened
 con.send(Reply.encode())
 #NOTE, this only takes encoded data

#Always close sockets after using
conn.close()
