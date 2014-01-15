from multiprocessing import Process
import socketserver
import socket

BUFFER_SIZE = 2048
HOST = "localhost"
PORT = 1234

class requestHandler(socketserver.BaseRequestHandler):
	def handle(self):
		message = self.request.recv(BUFFER_SIZE)
		message = message.decode("utf-8")
		address = self.client_address[0]
		port = self.client_address[1]
		print("Server received:", message, "from", address, ":", port)
		self.request.sendall(bytes("pong","utf-8"))

	def finish(self):
		self.server.shutdown()

def runServer():
	server = socketserver.TCPServer((HOST, PORT), requestHandler)
	server.serve_forever()

def runClient():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	sock.sendall(bytes("ping","utf-8"))
	reply = sock.recv(BUFFER_SIZE)
	reply = reply.decode("utf-8")
	print("Client received:", reply)

if __name__ == '__main__':
	server = Process(target = runServer)
	client = Process(target = runClient)
	server.daemon = True
	server.start()
	client.start()
	client.join()