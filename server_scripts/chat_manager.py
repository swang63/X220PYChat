from random import randint

class ChatManager:
	"""
	chat for server
	purpose is to:
		- store chat messages
		- store users
		
		- send back all chat messages
		- send backk all active users
	"""
	def __init__(self):
		self.chat_messages = []
		self.users = {}

	def insert_message(self, message):
		self.chat_messages.append(message)
		
	def return_messages(self) -> str:
		all_messages = ""
		
		for message in self.chat_messages:
			all_messages = all_messages + message + '\n'
			
		return all_messages
    
	def set_address(self, address):
		if address in self.users.keys():
			pass
		else:
			new_address_flag = True
			new_user = ""
			
			for _ in range(5):
				next_num = randint(0, 9)
				new_user += (str(next_num))
					
			while new_address_flag:
				if new_user in self.users.values():
					new_user = ""
					
					for _ in range(5):
						next_num = randint(0, 9)
						new_user += (str(next_num))
				else:
					new_address_flag = False
					
			self.users[address] = new_user

	def get_user(self, address):
		try:
			return self.users[address]
		except:
			print("No user ID was found!")
			self.set_address(address)
			return get_user(address)
		