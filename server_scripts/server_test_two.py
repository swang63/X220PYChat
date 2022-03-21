from gate_socket import GateSocket
from chat_manager import ChatManager
import sys

MAX_BYTE_SIZE = 1024

if len(sys.argv) != 2:
   exit()
   
address = str(sys.argv[1])

chat = ChatManager()
gate = GateSocket(address)

gate.bind()

while True:
   connectionSocket, addr = gate.accept()
   sentence = connectionSocket.recv(MAX_BYTE_SIZE).decode()
   
   # SEND TO CHAT OBJECT
   chat.insert_message(sentence)
   allSentences = chat.return_messages()
   
   connectionSocket.send(allSentences.encode())
   print(allSentences)

gate.close()
