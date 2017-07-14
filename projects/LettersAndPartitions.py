import functools

def letters(K):
	qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
	def solve(K, i, Z):
		if K == 0:
			print(K)
		else:
			for i in range(i+1, len(qwerty)-K+1):
				solve(K-1, i+1, Z+qwerty[i])


	solve(K, 0, "")

def partitions(K):
	qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
	def solve(K, i, Z):
	if K == 1:
		print(Z+"/"+qwerty[start:]+"/")
	else:
		for i in range(i+1, len(qwerty)-K+1):
			solve(K-1, i+1, Z+"/"+qwerty[start:i])


	solve(K, 0, "")

#qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
#for i in range(len(qwerty)-3);
#	for j in range(i+1, len(qwerty-2):
#		for k in range(j+1, len(qwerty)):
#			for m in range(k+1, len(qwerty)):
#				print(qwerty[i] + qwerty[j] + qwerty[k] + qwerty[m])
letters(4)
