from gate_socket import GateSocket
from chat_manager import ChatManager

import sys
import selectors

MAX_BYTE_SIZE = 4096
TOTAL_SOCKETS = 2

socket_list = []
chat = ChatManager()

sel = selectors.DefaultSelector()

def accept(gate, mask):
	connectionSocket, addr = gate.accept()

	chat.set_address(addr[0])
	
	connectionSocket.setblocking(False)
	sel.register(connectionSocket, selectors.EVENT_READ, read)
	
def read(connection, mask):
	sentence = connection.recv(MAX_BYTE_SIZE)
	host, port = connection.getpeername()
	
	if sentence:
		sentence = sentence.decode()
		split_sentence = sentence.split(": ", 1)
		
		#FOR COMMANDS
		if (split_sentence[1][0] == '/'):
			command = split_sentence[1][1:]
			
			#SWITCH OF COMMANDS
			commands = {
				"get_users": chat.get_usernames(),
				"get_messages": chat.return_messages()
			}
			
			command_result = commands.get(command, "No command selected")
			
			connection.send(command_result.encode())
		
		#FOR MESSAGES
		else:
			# GET THE IP's CHAT NUMBER
			chat_number = chat.get_user(host)
			
			chat.set_username(chat_number, split_sentence[0])
			
			# SEND TO CHAT OBJECT
			sentence = "[" + str(chat_number) + "] " + sentence
			chat.insert_message(sentence)
			allSentences = chat.return_messages()
			   
			confirm_chat = "Message accepted"
			
			connection.send(confirm_chat.encode())
			print(allSentences)
	else:
		sel.unregister(connection)
		connection.close()

# incase of no IP
# if len(sys.argv) != 2:
#   exit()
   
# address = str(sys.argv[1])
address = "0.0.0.0"

gate = GateSocket(address)
gate.bind(0)

sel.register(gate.get_socket(), selectors.EVENT_READ, accept)

#while True:
#	for g in socket_list:
#	   connectionSocket, addr = g.accept()
#	   connectionNumber = g.get_number()
#	   
#	   # connectionSocket.setblocking(False)
#	   
#	   sentence = connectionSocket.recv(MAX_BYTE_SIZE).decode()
#	   sentence = "[" + str(connectionNumber) + "] " + sentence
	   
	   # SEND TO CHAT OBJECT
#	   chat.insert_message(sentence)
#	   allSentences = chat.return_messages()
	   
#	   connectionSocket.sendall(allSentences.encode())
#	   print(allSentences)

# gate.close()

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

gate.close()
