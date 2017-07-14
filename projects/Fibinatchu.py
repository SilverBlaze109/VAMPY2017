import functools

num_plusses = 0

@functools.lru_cache(maxsize=None)
def bad_fib(N):
	global num_plusses
	if N < 2:
		return N
	else:
		num_plusses += 1
		return bad_fib(N-1) + bad_fib(N-2)
		print(bad_fib(100))
		print(num_plusses)

def countfast(N):
	counts = [0, 0]
	for i in range(2, N + 1):
		counts.append(counts[i-1]+counts[i-2]+1)
	return counts[N]

def countfaster(N):
	counts = [0, 1]
	for i in range(2, N + 1):
		counts.append(counts[i-1]+counts[i-2])
	return counts[N]

def bestcount(N):
	if N < 2:
		return N
	fib1 = 1
	fib2 = 0
	fib  = 1
	for i in range(2, N + 1):
		fib = fib1 + fib2
		fib2 = fib1
		fib1 = fib
	return fib
