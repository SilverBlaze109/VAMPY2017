import socket

while True:
#	N = input("Who are you calling? ")
	msg = input("What do you want to say? ")
	addr = ("vampy-cs-17", 8080)
	data = msg.encode("UTF-8")
	phone = socket.socket()
	phone.connect(addr)
	phone.send(data)
	resp = bytes.decode(phone.recv(1024))
	if resp != "r":
		print("ERROR ALL OUR BASE ARE BELONG TO US")
	phone.close()
