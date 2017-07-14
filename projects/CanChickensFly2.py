def tree(val):
	return [None, val, None]

def data(node, val = None):
	if node == None:
		return None
	elif val is None:
		return node[1]
	else:
		return node[1]

def yes(node, child = None):
	if node is None:
		return None
	elif child is None:
		return node[0]
	else:
		node[0] = child

def no(node, child = None):
	if node is None:
		return None
	elif child is None:
		return node[2]
	else:
		node[2] = child

root = tree("Am I an object or a place? (YES/NO): ")


yes(root, tree("Am I bigger than a PC? (YES/NO): "))
no(root, tree("Am I human? (YES/NO): "))


yes(yes(root),      tree("Am I a building? (YES/NO): "))
no(yes(root),       tree("Am I consumed as you use me? (YES/NO): "))
yes(no(root),       tree("Am I fictional? (YES/NO): "))
no(no(root),        tree("Can you fir me in a coffee mug? (YES/NO): "))


yes(yes(yes(root)), tree("Am I a salon? (YES/NO): "))
no(yes(yes(root)),  tree("Am I New York (YES/NO): "))
yes(no(yes(root)),  tree("Am I pizza? (YES/NO): "))
no(no(yes(root)),   tree("Am I a hat? (YES/NO): "))

yes(yes(no(root)),  tree("Am I Santa Clause? (YES/NO): "))
no(yes(no(root)),   tree("Am I Michael Jackson? (YES/NO): "))
yes(no(no(root)),   tree("Am I a rat? (YES/NO): "))
no(no(no(root)),    tree("Am I Dracula? (YES/NO): "))




yes(yes(yes(yes(root))), tree("I'M A SALON!"))
yes(no(yes(yes(root))),  tree("I'M NEW YORK!"))
yes(yes(no(yes(root))),  tree("I'M A PIZZA!"))
yes(no(no(yes(root))),   tree("I'M A HAT!"))

yes(yes(yes(no(root))),  tree("I'M SANTA!!! HO HO HO!!!"))
yes(no(yes(no(root))),   tree("I'M MICHAEL JACKSON! BRING ME FLOWERS!"))
yes(yes(no(no(root))),   tree("I'M A RAT! OMNOMNOM"))
yes(no(no(no(root))),    tree("I'M DRACULA!"))

no(yes(yes(yes(root))), tree("I'M A BOWLING ALLEY!"))
no(no(yes(yes(root))),  tree("I'M AN UMBRELLA!"))
no(yes(no(yes(root))),  tree("I'M A BAR OF SOAP!"))
no(no(no(yes(root))),   tree("I'M A COMPUTER!"))

no(yes(yes(no(root))),  tree("I'm Bond, James Bond."))
no(no(yes(no(root))),   tree("I'M BRITANNY SPEARS!"))
no(yes(no(no(root))),   tree("I'M A FROG!"))
no(no(no(no(root))),    tree("I'M A CHICKEN!!! DON'T EAT ME!!! I CAN'T FLY!!!"))

tracker = root
while"?" in data(tracker):
	answer = input(data(tracker))
	if answer == "YES":
		tracker = yes(tracker)
	else:
		tracker = no(tracker)


print(data(tracker))

