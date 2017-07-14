import socket
Team = [3, ,7 ,11]

phone = socket.socket()
phone.bind("vampy-cs-15", 8081)
phone.listen(5)
while True:
	try:
	except:	
		msg = input("Msg: ")
		addr = ("vampy-cs-7", 8081)
		data = msg.encode("UTF-8")
		phone.connect(addr)
		phone.send(data)
		resp = bytes.decode(phone.recv(1024))
		if resp != "r":
			print("ERROR ALL OUR BASE ARE BELONG TO US")








phone = socket.socket()
addr = (socket.gethostname(),8081)
phone.bind(addr)
phone.listen(5)
while True:
	try:
		conn, cid = phone.accept()
		msg = bytes.decode(conn.recv(1024))
		conn.send("r".encode("UTF-8"))
		conn.close()
		print("Call from {0}: {1}".format(cid, msg))
	except KeyboardInterrupt:
		print("Shutting down...")
		phone.close()
		break
	except:
		print("it broke")
		phone.close()
		break
