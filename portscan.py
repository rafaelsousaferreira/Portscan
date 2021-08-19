#!/usr/bin/python


import socket
import sys

# Meu terceiro script
if len(sys.argv) <= 2 :

	print "Modo de uso: 192.168.100.1 80"

else :
	ip = sys.argv[1]
	porta = int(sys.argv[2])

	meusocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	resp = 0
	resp = meusocket.connect_ex((ip,porta))

if (resp == 0) :

	print "[PORTA ABERTA]"

else :

	print "[PORTA FECHADA] "
