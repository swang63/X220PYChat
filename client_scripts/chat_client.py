# import Kivy
import kivy
import random

from kivy.app import App
from kivy.lang.builder import Builder

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty



from client_socket import ClientSocket

import sys

IP_address = "144.202.8.209"

client = ClientSocket(IP_address)


chat_layout = Builder.load_file('chat_gui.kv')

class ChatGrid(Widget):
	username = ObjectProperty(None)
	message = ObjectProperty(None)
	
	user_list = ObjectProperty(None)
	chat_log = ObjectProperty(None)
	
	def get_users(self):
		print("Get Users")
		
		self.user_list.text = client.send("", "/get_users")
		
	def send_message(self):
		user_to_send = self.username.text
		message_to_send = self.message.text
		
		user_test = user_to_send.replace(" ", "")
		message_test = message_to_send.replace(" ", "")
		
		if (message_test != "" and user_test != ""):
			client.send(self.username.text, self.message.text)
			
		self.message.text = ""
		
		self.chat_log.text = client.send("", "/get_messages")


class ChatClient(App):
    def build(self):
        return ChatGrid()



if __name__ == "__main__":
	client.connect()

	ChatClient().run()
	
	client.close()
	
