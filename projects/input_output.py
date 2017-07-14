origin = []
revorigin = []
z = 0
a = []

ans = input("What number to test? ")
ans = ans.split()

for i in ans:
	origin.append(i)

while True:
	revorigin = origin
	x = len(revorigin)
	if x % 2 == 0:
		y = x/2
	if x % 2 == 1:
		y = (x - 1) / 2
	while y != 0:
		a.append(origin[0])
		origin.pop(0)
		origin.append(a[0])
		y = y - 1
	if revorigin != origin:
		origin[len(origin) - 1] = int(origin[len(origin)-1]) + 1
		revorigin[0] = int(revorigin[0]) + 1
		print(origin)
		continue
	if revorigin == origin:
		print(origin)
		break
