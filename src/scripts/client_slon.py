import socket
import time

from src.scripts.UI.gameWindow import GameWindow
from src.scripts.game_dir.gameCoordinator import ClientGameCoordinator


class Client:
	def __init__(self, client_UI):
		self.__client_UI = client_UI
		self.__socket = socket.socket()
		self.__client_UI.button_confirm.clicked.connect(self.connect_to_server)

	def connect_to_server(self):
		hostname = self.__client_UI.get_entered_hostname()
		port = self.__client_UI.get_entered_port()
		hostname = hostname if hostname else "mamin_papa_ded"
		try:
			self.__socket.connect((hostname, port))
			time.sleep(0.5)
			self.on_connect()
			self.__client_UI.close()
			return True
		except Exception as e:
			print(e)
			return False

	def on_connect(self):
		gw = GameWindow()
		gw.show()
		ClientGameCoordinator(self, gw)
		self.__client_UI.destroy()

	def send_message_to_server(self, msg):
		self.__socket.send(msg.encode())

	def get_message_from_server(self):
		return self.__socket.recv(1024)
