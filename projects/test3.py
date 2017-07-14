import Merge_Sorting

NAME = []

read_filename = "/home/vampy/data/list"
fp = open(read_filename, "r")
M = int(fp.readline())

for i in range(M):
	NAME.append(fp.readline().strip())

fp.close()

Merge_Sorting.mergesort(NAME)

print("First: " + NAME[0] + "\n" + "Third: " + NAME[2] + "\n" + "Last: " + NAME[4])
