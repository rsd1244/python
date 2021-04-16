#!/usr/bin/python

import socket, ipaddress, time

startTime = time.time()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(5)

try:
    host = input("Enter the IP address you would like to scan: ")
    ip = ipaddress.ip_address(host)
    print(f'{ip} is correct. Version: IPv{ip.version}')
except ValueError:
    print("Address is invalid")

port = int(input("Enter the port number to scan: "))

def portscanner(port):
    if sock.connect_ex((host,port)):
        print("Port %d is closed" % (port))
    else:
        print("Port %d is open" % (port))
print('Time take:', time.time() - startTime)

portscanner(port)
