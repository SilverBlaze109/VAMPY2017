def old_exponent(n, k):
	n = int(input("N: "))
	k = int(input("N: "))

	answer = 1
	for i in range (k):
		answer *=n

	print(answer)

def fast_exponent(n, k):
	print("fast_exponent({0},{1})".format(n, k))
	if k == 1:
		return n
	elif k == 0:
		return 1

	left = int(k/2)
	right = k - left
	return fast_exponent(n, left) * fast_exponent(n, right)
