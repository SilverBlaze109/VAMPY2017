import random as r

num = r.randint(1,100)

while True:
	guess = input("Guess a Number? ")

	if(guess == str(num)):
		print("You Win")
		break
	elif(int(guess) > num):
		print("lower")
	else:
		print("higher")
