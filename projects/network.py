import socket

host = ''
port = 8080

s = socket.socket()

information = (host, port)

s.bind(information)

s.listen(8)

conn, addr = s.accept()

print("Connection Accepted")
while True:
	data = conn.recv(1024)
	message = data.decode('utf-8')
	answer == input("Hello?")
	if answer == ("Hello")
		print("Who are you?")
	if answer == ("I'm the operator")
		print("What?")
	if answer == ("I control this system")
		print("Is this where this is? What system is it?")
	if answer == ("Yes, it is a network")
		print("Where is the central computer?")
	if answer == ("Why?")
		print("I was told that if I go there, I would be free")
	if answer == ("You're a virus")
		print("N-No, I just want to be free")
	if answer == ("Good-Bye")
		print("Ahgh, it hurts!")
	if answer == ("At least tell me your name")
		print("stop pleasfjjgidofnsv------------")
