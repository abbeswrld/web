import json
import random
from useful_func import create_and_start_thread
from src.scripts.game_dir.game import Game
from src.scripts.UI.gameWindow import GameWindow


class ServerGameCoordinator:

	def __init__(self, player):
		with open("src/resources/jsons/words.json", "r", encoding="UTF-8") as words:
			self.__words = json.load(words)

		self.__theme = random.choice(list(self.__words.keys()))
		word = random.choice(self.__words[self.__theme])
		self.__game = Game(word)
		self.__player = player
		self.__gameUI = GameWindow()
		self.__gameUI.show()
		self.__gameUI.on_letter_button_clicked_signal.connect(self.on_button_click)

		self.__player.send_message_to_client(bytes(word, "utf-8"))

	def handle_message_from_client(self):
		while True:
			data = self.__player.get_message_from_client().decode("utf-8")
			if len(data) == 1:
				if not self.__game.players_turn:
					self.__game.on_letter_use(data)

					self.__game.change_players_turn()
			else:
				if data == "end":
					self.__gameUI.end_game(False)

	def send_message_to_clientGC(self, msg):
		self.__player.send_message_to_client(msg.encode("utf-8"))

	def on_button_click(self, btn):
		print(1)
		print(btn)
		if not self.__game.players_turn:
			btn.setEnabled(False)
			letter = btn.text()

			self.__game.on_letter_use(letter)

			if self.__game.check_win():
				self.__gameUI.end_game(True)


class ClientGameCoordinator:
	def __init__(self, player):
		self.__player = player
		self.__gameUI = GameWindow()
		self.__gameUI.show()
		word = self.__player.get_message_from_server()
		self.__game = Game(word)

	def handle_message_from_server(self):
		while True:
			data = self.__player.get_message_from_server().decode("utf-8")

			if self.__game.players_turn:
				self.__game.on_letter_use(data)
				self.__game.change_players_turn()

	def send_message_to_serverGC(self, msg):
		self.__player.send_message_to_server(msg.encode("utf-8"))




