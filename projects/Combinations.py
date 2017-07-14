import random
id = 0
tops = ["AE","Vampy","Hollister","Polo"]
bottoms = ["Khakis","Blue Jeans","AE Brown Shorts","AE Blue Shorts","AE Black Shorts"]
shoes = ["Sparry","Adidas"]
headgear = ["None","Morehead Hat","Sunglasses"]
socks = ["Black"]

pattern = "#{0}: Top={1}, Bottom={2}, Shoes={3}, Head={4}, Socks{5}"
for top in tops:
	for bottom in bottoms:
		for kicks in shoes:
			for headitem in headgear:
				for pair in socks:
					id += 1
					print(pattern.format(id, top, bottom, kicks, headitem, pair))

top = random.sample(tops, 1)[0]
bottom = random.sample(bottoms, 1)[0]
kicks = random.sample(shoes, 1)[0]
headitem = random.sample(headgear, 1)[0]
pair = random.sample(socks, 1)[0]
print(pattern.format("random", top, bottom, kicks, headitem, pair))
