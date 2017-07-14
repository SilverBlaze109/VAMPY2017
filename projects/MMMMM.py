def mode(nums):
	"""
	nums must be array like mode[1,2,3,1] == 1
	mena runs in O(N) time where N = len(nums)
	"""
	tally = {}
	M = nums[0]
	for x in nums:
		tally[x] = tally.get(x ,0) + 1
		if tally[x] > tally[M]:
			M = x
	return M


#print("The mode is "+str(mode([1,2,3,1,2,3,1,]))


def mean(nums):
	if len(nums) == 0:
		return NONE
	M = 0
	for x in nums:
		M += x

	M /= len(nums)
	return M

def maximum(nums):
	M = nums[0]
	for x in nums:
		if x > M:
			M = x

	return M

def minimum(nums):
	M = nums[0]
	for x in nums:
		if x < M:
			M = x

	return M

def median(nums):
	temp = sorted(nums)
	if len(temp) % 2 == 0:
		mid1 = int(len(temp) / 2) - 1
		mid2 = int(len(temp) / 2)
		return (temp[mid1] + temp[mid2]) / 2
	else:
		mid = int(len(temp)/2)
		return temp[mid]


















