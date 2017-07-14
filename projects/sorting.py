
def bubbles(items):
	for t in range(len(items) - 1):
		for i in range(len(items) - 1):
			if items[i] > items[i + 1]:
				temp = items[i]
				items[i] = items[i + 1]
				items[i + 1] = temp

def reversebubble(items):
	for t in range(len(items) - 1):
		for i in range(len(items) - 1):
			if items[1] < items[i + 1]:
				temp = items[i]
				items[i] = items[i + 1]
				items[i + 1] = temp

"""
MAKE SURE TO TYPE LIST TO SHOW SORTED LIST
EX:
>>>my_list = [ blah bleh blah]
>>>sorting.bubbles(my_list)
>>>my_list
>>>[ blah blah bleh ]
