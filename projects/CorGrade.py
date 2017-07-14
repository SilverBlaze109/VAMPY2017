def max_partition_sum(S,K):
	if K == 1:
		return int(S)
	else
		maxSum = 0
		i = 1
		Z = int(S[:i])
		while Z <= 100 and i < lens(S):
			tmpSum = Z + max_partition_sum(S[i:], K - 1)
			if tmpSum > maxSum:
				maxSum = tmpSum
			
			i += 1
			Z = int(S[:i])
		
		return maxSum

filename = "..."
fp = open(filename, "r")
C = int(fp.readline())
for t in range(C):
	line = fp.readline().strip()
	data = line.split()
	K = int(data[0])
	S = data[1]
	print(round(max_partition_sum(S, K) / K))
