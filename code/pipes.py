from multiprocessing import Process, Pipe

def createFilter(func, inc, out):
	while True:
		arg = inc.recv()
		res = func(arg)
		out.send(res)

# pIn =pipe= pOut FUNC toNext =pipe= pEnd
def createProcesses(functions):
	pIn, pOut = Pipe() 
	pipeLineIn = pIn

	for f in functions:
		(toNext, pEnd) = Pipe()
		p = Process(
				target = createFilter,
				args = (f, pOut, toNext))
		p.daemon = True
		p.start()
		pOut = pEnd
	return(pipeLineIn, pEnd)

def split(str): return str.split(' ')

def capitalize(lst): return list(map(lambda s: s.capitalize(), lst))

def merge(lst):
	res = ""
	for s in lst: res += s
	return res

def decapitalizeFirst(str):
	head = str[0]
	tail = str[1:]
	return head.lower() + tail

if __name__ == '__main__':
	lst = [split, capitalize, merge, decapitalizeFirst]
	t = createProcesses(lst)
	begin = t[0]
	end = t[1]

	begin.send("Make this sentence camelCase")
	res = end.recv()
	print(res)