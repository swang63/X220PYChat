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
		self.users = []
		
	def insert_message(self, message):
		self.chat_messages.append(message)
		
	def return_messages(self) -> str:
		all_messages = ""
		
		for message in self.chat_messages:
			all_messages = all_messages + message + '\n'
			
		return all_messages
    