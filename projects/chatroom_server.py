import socket

phone = socket.socket()
addr = (socket.gethostname(),8080)
phone.bind(addr)
phone.listen(17)
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
