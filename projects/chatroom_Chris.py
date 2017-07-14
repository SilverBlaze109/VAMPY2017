import socket
import _thread


port = int(input("Enter a port to host on: ")

def handle_connection(conn, addr):
	while True:
		data = conn.recv(1024)
		print(data.decode("UTF-8"))
		
address = ""
port = int(input("Enter a port to host on: ")
s = socket.socket()
s.bind((address.port))

s.listen(18)

conn , addr = s.accept()

while True:
	conn, addr = s.accept()
	_thread.start_new_thread(handle_connection, (conn, addr))
