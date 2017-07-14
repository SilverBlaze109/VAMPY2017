import socket
import time

def client():
	while True:
		N = input("Who are you calling? ")
		msg = input("What do you want to say? ")
		addr = ("vampy-cs-17", 8080)
		data = msg.encode("UTF-8")
		phone = socket.socket()
		try:
			phone.connect(addr)
			phone.send(data)
			resp = bytes.decode(phone.recv(1024))
			phone.close()
		if resp != "r":
			print("ERROR ALL OUR BASE ARE BELONG TO US")
		phone.close()

def server():
	addr= (socket, gethostname(), 8080)
	store = socket.socket()
	store.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	store.bind(addr)
	store.listen(128)
	while True:
		try:
			phone, cide = store.accept()
			msg = bytes.decode(phone.recv(1024))
			phone.close()
			print("Call form {0}: {1}".format(cid, msg))
		except KeyboardInterrupt:
			print("Shutting down...")
			break

t1 = threading.Thread(target = server)
t2 = threading.Thread(target = client)

t1.start()
t2.start()

t1.join()
t2.join()
