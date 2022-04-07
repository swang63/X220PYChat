from client_socket import ClientSocket

import sys

# if len(sys.argv) != 2:
#    print ("Correct usage: script, IP address")
#    exit()
	
# IP_address = str(sys.argv[1])

# would put in .env file, but this is mostly a showcase

IP_address = "144.202.8.209"

client = ClientSocket(IP_address)
client.connect()

flag = True

sentence = None

while (flag):
	sentence = input("Type a sentence:")

	if (sentence == "/exit"):
		flag = False
	else:
		client.send("Some Nutter", sentence)

client.close()
