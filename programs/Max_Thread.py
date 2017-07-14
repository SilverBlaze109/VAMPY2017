import _thread
import threading
import random

a = 0
b = 0
c = 1
d = 0
m_a = ""

array = []

while a < 1000:
	y = random.randint(1, 1001)
	array.append(y)
	a = a + 1

def max_array(name, delay):
	global b
	global c
	global d
	while d < 1000:
		if array[b] > array[c]
			array[b] = m_a
			b = b + 1
			c = c + 1
			d = d + 1
		if array[b] < array[c]
			array[c] = m_a
			b = b + 1
			c = c + 1
			d = d + 1
		if array[b] = array[c]
			arracy[c] = m_a
			b = b + 1
			c = c + 1
			d = d + 1



_thread.start_new_thread(max_array, ("T1", 1))
_thread.start_new_thread(max_array, ("T2", 1))
_thread.start_new_thread(max_array, ("T3", 1))
_thread.start_new_thread(max_array, ("T4", 1))
