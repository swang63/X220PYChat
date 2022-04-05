from client_socket import ClientSocket

import sys

if len(sys.argv) != 2:
    print ("Correct usage: script, IP address")
    exit()
	
IP_address = str(sys.argv[1])

client = ClientSocket(IP_address)
client.connect()

flag = True

sentence = None

while (flag):
	sentence = input("Type a sentence:")

	if (sentence == "/exit"):
		flag = False
	else:
		client.send("User", sentence)

client.close()