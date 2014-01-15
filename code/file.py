from multiprocessing import Process, Lock

path = 'names.txt'

def leaveName(name, lock):
	name = str(name) + '\n'
	with lock:
		f = open(path, 'a')
		f.write(name)

def getNames(lock):
	with lock:
		f = open(path, 'r')
		str = f.read()
	return str.strip().split('\n')

def discover(name, members, lock):
	leaveName(name, lock)
	print(name, "left name")
	names = []
	found = 0
	while found is not members:
		names = getNames(lock)
		found = len(names)
	print(name, "found:", names)

if __name__ == '__main__':
	open(path, 'w')
	processes = []
	lock = Lock()
	members = 5

	for idx in range(0, members):
		p = Process(
			target = discover,
			args = (idx, members, lock))
		p.start()
		processes += [p]
	for p in processes:
		p.join()
