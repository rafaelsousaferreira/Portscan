#!/usr/bin/python3


import socket,time,sys
from tqdm import tqdm
from termcolor import colored

if len(sys.argv) <= 1 :

	print "Modo de uso: 192.168.100.1 80"

else :
	
	for i in tqdm(range(0,65535)):
                time.sleep(0.1)
		ip = sys.argv[1]
		porta = i

		meusocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		resp = 0
		resp = meusocket.connect_ex((ip,porta))

		if (resp == 0) :

			print (colored("\n \n [PORTA ABERTA]-->",'red'),porta)
