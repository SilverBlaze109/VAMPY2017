N = int(input("How many players are playing? "))
stack = []

effect = input("What effect was just cast? ")
stack.append(effect)

while len(stack) > 0:
	P = 1
	while effect != "pass" or P <= N:
		effect = input("Player #{0}, do you respond or pass? " .format(P))
		if effect == "pass":
			P += 1
		else:
			stack.append(effect)
			P = 1

	resolving = stack.pop()
	print("Please resolve the effect if it was not countered: {0}".format(resolving))

print("Active player, your priority...")
