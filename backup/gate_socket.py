from socket import *

PORT = 8081

class GateSocket:
	"""
	socket for handshake
	purpose is to:
		- open connection for chat
		- send back a chat number
		- accept
	"""
	
	def __init__(self, server_IP):
		self.ser_socket = socket(AF_INET,SOCK_STREAM)
		self.IP_bind = server_IP
		
	def bind(self):
		self.ser_socket.bind((self.IP_bind,PORT))
		self.ser_socket.listen(1)
		print("The server is ready to receive")
		
	def accept(self):
		return self.ser_socket.accept()
		
	def close(self):
		self.ser_socket.close()