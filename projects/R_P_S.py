import random as r

num = r.radint(0,2)

0 = rock

1 = paper

2 = scissors

while True:
	guess = input("Rock Paper Scissors SHOOT! ")

	if(guess == str(num)):
		print("It's a Tie!")
	elif(guess == 0 and str(num) == 2):
		print("You Win!")
	elif(guess == 1 and str(num) == 0):
		print("You Win!")
	elif(guess == 2 and str(num) == 1):
		print("You Win!")
	else:
		print("You Lose!")

