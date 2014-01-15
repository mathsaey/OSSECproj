from threading import Thread, Condition
import random

resource = []
condVar = Condition()

def produce():
	global resource
	for ctr in range(0,100):
		with condVar:
			i = random.randint(0, 100)
			if i is 22: condVar.notify()
			resource += [i]

def consume():
	with condVar:
		while resource.count(22) is 0:
			condVar.wait()
		print("Lucky number 22 found!", resource)

if __name__ == '__main__':
	random.seed()

	producer = Thread(target = produce)
	consumer = Thread(target = consume)
	consumer.daemon = True
	producer.start()
	consumer.start()
	producer.join()