from gate_socket import GateSocket
import sys

if len(sys.argv) != 2:
   exit()
   
address = str(sys.argv[1])

gate = GateSocket(address)

gate.bind()

while True:
   connectionSocket, addr = gate.accept()
   sentence = connectionSocket.recv(1024).decode()
   capitalizedSentence = sentence.upper()
   connectionSocket.send(capitalizedSentence.encode())
   print(capitalizedSentence)

gate.close()
