N = int(input("Gimme a number: "))

isPrime = True

for test in range(2, int(N/2)+1):
	if N % test == 0:
		isPrime = False
		print("{0} is a factor.".format(test))

if isPrime:
	print("It is prime")
else:
	print("It is not prime")
