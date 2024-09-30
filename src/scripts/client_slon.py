import socket
import time
from src.scripts.UI.gameWindow import GameWindow
from src.scripts.game_dir.gameCoordinator import ClientGameCoordinator
from src.scripts.music_player import MusicPlayer


class Client:
	def __init__(self, client_UI):
		self.__client_UI = client_UI
		self.__socket = socket.socket()
		self.__client_UI.button_confirm.clicked.connect(self.connect_to_server)
		self.__musicPlayer = MusicPlayer()

		self.__musicPlayer.play_sound("auto")

	def connect_to_server(self):
		hostname = self.__client_UI.get_entered_hostname()
		port = self.__client_UI.get_entered_port()
		hostname = hostname if hostname else "mamin_papa_ded"
		self.__socket.connect((hostname, port))
		self.on_connect()

	def on_connect(self):
		self.__gw = GameWindow()
		self.__gw.show()
		self.__cgc = ClientGameCoordinator(self, self.__gw)
		self.__client_UI.destroy()

	def send_message_to_server(self, msg: bytes) -> None:
		self.__socket.send(msg)

	def get_message_from_server(self):
		return self.__socket.recv(1024)
