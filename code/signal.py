from multiprocessing import Process
from time import sleep
import signal
import os

# The kill signal is different depending
# on the platform we are running on
def getKillSig():
	try:
		return signal.SIGKILL
	except AttributeError:
		return signal.CTRL_C_EVENT

def guardProcess(process, timeout):
	sleep(timeout)
	if process.is_alive():
		pid = process.pid
		os.kill(pid, getKillSig())
		print("Process killed...")
		os._exit(1)
	else:
		print("Process finished...")
		os._exit(0)

def longProcess():
	sleep(60)

if __name__ == '__main__':
	process = Process(target = longProcess)
	process.start()
	guardProcess(process, 2)