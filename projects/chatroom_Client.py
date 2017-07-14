import socket

address = input("Enter address: ")
port = int(input("Enter port: "))

s = socket.socket()

s.connect((address, port))

while True:
	message = input("Msg: ")
	s.sendall(message.encode("UTF-8"))
