
A = 1
B = 2
I_Counter = 0
Island_Ray = []
Z = 1

filename = "islandlist"
fp = open(filename, "r")
K = int(fp.readline())
for t in range(K):
	Island_Ray = fp.readline().strip()
	Island_Ray = Island_Ray.split()

	while True:
		if B == 16:
			break
		if int(Island_Ray[A]) - int(Island_Ray[B]) == 1:
			I_Counter += 1
			A = A + 1
			B = B + 1
			continue
		if int(Island_Ray[A]) - int(Island_Ray[B]) != 1:
			A = A + 1
			B = B + 1
			continue

	print( "{0} {1}\n".format(Z, I_Counter) )
	A = 0
	B = 1
	I_Counter = 0
	Z = Z + 1
