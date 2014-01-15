from threading import Semaphore, Thread
from time import sleep
import random

def access(idx, sem):
	with sem:
		print(idx, "starting critical section")
		sleep(random.randint(0,3))
		print(idx, "finished critical section")

if __name__ == '__main__':
	random.seed()
	threads = []
	sem = Semaphore(3)

	for idx in range(0, 10):
		t = Thread(
			target = access,
			args = (idx, sem))
		t.start()
		threads += [t]
	for t in threads:
		t.join()
