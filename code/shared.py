from multiprocessing import Process, Value, Array
from time import sleep
import random

def runProcess(arr, remainActive):
	while remainActive.value:
		for idx in range(len(arr)):
			arr[idx] = random.randint(0,100)
		sleep(1)

def runMonitor(arr, remainActive):
	while remainActive.value:
		print(arr[:])
		sleep(2)

if __name__ == '__main__':
	random.seed()
	arr = Array('i', range(5))
	remainActive = Value('i', 1)

	process = Process(target = runProcess, args = (arr, remainActive))
	monitor = Process(target = runMonitor, args = (arr, remainActive))
	process.daemon = True
	monitor.daemon = True
	process.start()
	monitor.start()

	sleep(10)
	remainActive.value = 0

	process.join()
	monitor.join()