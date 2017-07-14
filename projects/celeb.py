connections = {}
connections["Joj"] = []
connections["Emily"] = ["Joj","Jeph","Jeff"]
connections["Jeph"] = ["Joj","Geoff"]
connections["Jeff"] = ["Joj","Judge"]
connections["Geoff"] = ["Joj","Jebb"]
connections["Jebb"] = ["Joj","Emily"]
connections["Judge"] = ["Joj","Judy"]
connections["Jodge"] = ["Joj","Jebb","Stephan","Judy"]
connections["Judy"] = ["Joj","Judge"]
connections["Stephan"] = ["Joj","Jodge"]

names = ["Emily","Jeph","Jeff","Geoff","Jebb","Judge","Jodge","Judy", "Joj","Stephan"]

candidate = names[0]
for i in range(1, len(names)):
	if names[i] in connections[candidate]:
		candidate = names[i]

print("Our best candidate is {0}".format(candidate))

for name in names:
	if name != candidate and name in connections[candidate]:
		print("The candidate is a lie!")
		exit()
	elif name != candidate and candidate not in connections[name]:
		print("The candidate is a lie, they are not known by somebody!")
		exit()

print("We made it to the end, the celebrity is the real deal.")
