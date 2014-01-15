from multiprocessing import Process, Queue

def workProcess(inQueue, outQueue):
	while True:
		tuple = inQueue.get()
		func = tuple[0]
		args = tuple[1]
		res = func(*args)
		outQueue.put(res)

def sendFunction(function, args, inQueue, outQueue):
	inQueue.put((function, args)),
	return outQueue.get()

def aFunction(x,y): return x + y

if __name__ == '__main__':
	inQueue = Queue()
	outQueue = Queue()

	worker = Process(
		target = workProcess,
		args = (inQueue, outQueue))
	worker.daemon = True
	worker.start()

	r = sendFunction(
		aFunction,
		(3,4),
		inQueue,
		outQueue)

	print(r)