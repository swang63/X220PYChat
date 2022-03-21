from socket import *

PORT = 8081

class ClientSocket:
	"""
	socket for client
	purpose is to:
	- connect to server sockets
	- send strings
	- get back chat log
	- get back users
	- get back user number
	
	generally speaking, this is the backend of the client program
	"""
	
	def __init__(self, server_IP):
		self.cli_socket = socket(AF_INET, SOCK_STREAM)
		self.IP_to_connect_to = server_IP
		
	def connect(self):
		self.cli_socket.connect((self.IP_to_connect_to, PORT))
		
	def send(self, number, name, message):
		sentence = "[" + str(number) + "] " + name + ": " + message
		self.cli_socket.send(sentence.encode())
		modifiedSentence = self.cli_socket.recv(1024)
		print ("From Server:", modifiedSentence.decode())
	
	def close(self):
		self.cli_socket.close()
	