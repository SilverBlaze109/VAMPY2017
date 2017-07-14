import _thread
import time
import threading

counter = 0
lock = threading.Lock()

def counter_work(name, delay):
	global counter
	global lock
	while counter < 1000:
		time.sleep(delay)
		lock.aquire()
		counter += 1
		print(counter, name)
		lock.release()

_thread.start_new_thread(counter_work, ("T1", 1))
_thread.start_new_thread(counter_work, ("T2", 1))
_thread.start_new_thread(counter_work, ("T3", 1))
_thread.start_new_thread(counter_work, ("T4", 1))
_thread.start_new_thread(counter_work, ("T5", 1))
_thread.start_new_thread(counter_work, ("T6", 1))
_thread.start_new_thread(counter_work, ("T7", 1))
_thread.start_new_thread(counter_work, ("T8", 1))

while counter < 1000:
	pass
