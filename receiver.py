#!/usr/bin/python2

import socket
rec_ip="127.0.0.1"
myport=9999
#                   ipv4,   UDP
#    only for rec
# below method with argument creating a socket called s
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#now connecting ip and port 
s.bind((rec_ip,myport))
#buffer size
while 4 >  2 :

             print  s.recvfrom(1000)
