import socket

s = socket.socket()
host = "138.197.75.197"
port = 12345

s.connect((host, port))
print s.recv(1024)
d = ""
while d != "exit()":
	d = raw_input(">>")
	s.send(d)
s.send("TERMINATE")
s.shutdown(socket.SHUT_RDWR)
s.close
