import socket
import thread
import os

def c_thread(c):
	print "Thread started"
	toReturn = 'Connection Successful'
	dz = str(z[1])
	toReturn = toReturn + " " + dz
	c.sendto(toReturn, z)
	data = ""
	while True:
		data = c.recv(1024)
		if data == "exit()":
			os._exit(1)
		print c.getpeername() , "Says: " ,data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_host = socket.gethostbyname_ex(socket.gethostname())[-1][0]
port = 12345
s.bind((local_host, port))
print "Server Host Address is: " + local_host
z = ''
while True:
	s.listen(5)
	c, address = s.accept()
	print "Successful connection from", address
	z = c.getpeername()
	thread.start_new_thread(c_thread, (c, ))

