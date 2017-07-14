import random
import time

names = ["Aaron","Bobb","Cyamper","Dylan","Enoch","Emily","Film","Geoff",
	 "Hailey","Inigo Montoya","Jacob","Joj","Kyle","Leroy Jenkins",
	 "Madom Zostra","Newt","Othello","Pigeon","Quincey"]

Q = []
for name in random.sample(names, 3):
	Q.append(name)

hour = 6
while len(Q) > 0:
	time.sleep(5)
	print("It is {0} o'clock, and there are {1} people at the diner!".format(hour, len(Q)))
	for i in range(random.randint(1, 20)):
		if len(Q) >= 20:
			leaving = Q.pop(0)
			print("{0} is leaving!".format(leaving))
		if len(Q) < 2:
			joining = random.choice(names)
			Q.append(random.choice(names))
		if random.uniform(0, 1) < 0.50:
			joining = random.choice(names)
			Q.append(random.choice(names))
			print("{0} is joining".format(joining))
			print("{0} is joining".format(joining))
		elif len(Q) > 0:
			leaving = Q.pop(0)
			print("{0} is leaving!".format(leaving))
	
	hour += 1

print("Closing up shop!")
