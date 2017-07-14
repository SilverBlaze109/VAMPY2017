f = open("Dictionary.txt", "w")

number = {"Jaj":7, "Emily":4, "Geoff":9}

sorted_num = sorted(number)
print(sorted_num)

for key in sorted_num:
	f.write(sorted_num[key])
