import threading
import random
import time

fruits = []
def produce():
	global fruits
	while True:
		fruit = random.randint(0, 100)
		fruits.append(fruit)
		print("I created the fruit #{0}".format(fruit))
		time.sleep(0.1)

def consume():
	global fruits
	while True:
		if len(fruits) > 0:
			fruit = fruits.pop(0)
			print("I ate the fruit#{0}".format(fruit))
			time.sleep(0.25)

t1 = threading.Thread(target = produce)
t2 = threading.Thread(target = consume)
t3 = threading.Thread(target = consume)

t1.start()
t2.start()
t3.start()
print("The threads should be running now.")
t1.join()
t2.join()
t3.join()
print("The threads should be done now.")
