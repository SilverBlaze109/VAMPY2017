
abet = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

A = 0
B = 1
C = 2
D = 3
A_Counter = 0
B_Counter = 0
answer = input("How many numbers in your combinations? ")
if answer == "1":
	print(abet)
if answer == "2":
	while True:
		if A == 25:
			break
		if A_Counter > A:
			A = A + 1
			B = B + 1
			continue
		if B == 26:
			A = 0
			B = 1
			A_Counter = A_Counter + 1
			continue
		if B < 26:
			print("{0} {1}\n".format(abet[A], abet[B]))
			B = B + 1
			continue
if answer == "3":
	while True:
		if A == 25:
			break
		if A_Counter > A:
			A = A + 1
			B = B + 1
			continue
		if C == 26:
			A = 0
			B = 1
			C = 2
			A_Counter = A_Counter + 1
			continue
		if C < 26:
			print("{0} {1} {2}\n".format(abet[A], abet[B], abet[C]))
			C = C + 1
			continue
