def countfast(N):
	counts = [0, 0]
	for i in range(2, N + 1):
		counts.append(counts[i-1]+counts[i-2]+1)
	return counts[N]
	
def fastcount(N):
	counts = [0, 1]
	for i in range(2, N + 1):
		counts.append(counts[i-1]+counts[i-2])
	return counts[N]
