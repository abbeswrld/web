import socket
import time

from src.scripts.UI.gameWindow import GameWindow
from src.scripts.game_dir.gameCoordinator import ClientGameCoordinator
from useful_func import create_and_start_thread


class Client:
	def __init__(self, client_UI):
		self.__client_UI = client_UI
		self.__socket = socket.socket()
		try:
			self.__client_UI.button_confirm.clicked.connect(self.connect_to_server)
		except Exception as e:
			print(e)

	def connect_to_server(self):
		try:
			hostname = self.__client_UI.get_entered_hostname()
			port = self.__client_UI.get_entered_port()
			hostname = hostname if hostname else "mamin_papa_ded"
			self.__socket.connect((hostname, port))
			self.on_connect()
		except Exception as e:
			print(e)

	def on_connect(self):
		ClientGameCoordinator(self)
		self.__client_UI.destroy()

	def send_message_to_server(self, msg):
		self.__socket.send(msg.encode())

	def get_message_from_server(self):
		return self.__socket.recv(1024)
