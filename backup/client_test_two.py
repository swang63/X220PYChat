from client_socket import ClientSocket

import sys

if len(sys.argv) != 2:
    print ("Correct usage: script, IP address")
    exit()
	
IP_address = str(sys.argv[1])

client = ClientSocket(IP_address)
client.connect()

sentence = input("Input lowercase sentence:")

client.send(1, "User", sentence)

client.close()