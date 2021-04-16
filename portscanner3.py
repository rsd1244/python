#!/usr/bin/python

import socket, ipaddress, time
from termcolor import colored
startTime = time.time()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(5)

try:
    host = input("Enter the IP address you would like to scan: ")
    ip = ipaddress.ip_address(host)
    print(f'{ip} is correct. Version: IPv{ip.version}')
except ValueError:
    print("Address is invalid")

#port = int(input("Enter the port number to scan: "))

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[!!] Port %d is closed" % (port), 'red'))
    else:
        print(colored("[+] Port %d is open" % (port),'green'))
print('Time take:', time.time() - startTime)

for port in range(100):
    portscanner(port)
