def doodad(x):
	if x == 0:
		return "Squarb"
	else:
		subsolution = doodad(x-1)
		solution = subsolution + "!"
		return solution
