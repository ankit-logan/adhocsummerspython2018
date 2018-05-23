#!/usr/bin/python2

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto("yo bro",("127.0.0.1",9999))
