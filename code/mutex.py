from multiprocessing import Process, Lock

def writeMessage(idx, message, lock):
	message = str(idx) + " mu: " + message + '\n'
	lock.acquire()
	f = open('mutexfile.txt', 'a')
	f.write(message)
	lock.release()

if __name__ == '__main__':
	processes = []
	lock = Lock()

	for idx in range(0, 10):
		p = Process(
			target = writeMessage,
			args = (idx, "writing to shared resource!", lock))
		p.start()
		processes += [p]
	for p in processes:
		p.join()