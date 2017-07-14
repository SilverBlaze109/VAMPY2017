
age = {"Emily":15, "Jaj":15, "Geoff": 12}

age2 = {"Jeff":14, "Jeph":16, "Jax":17}

print(age["Emily"] + age["Jaj"])

#age.update(age2);

def multiply_dictionary(diction, mult):
	for key in diction:
		diction[key] *= mult
	print(diction)

sorted_keys = sorted(age)
for key in sorted_keys:
	print(age[key])
