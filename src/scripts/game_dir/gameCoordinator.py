import json
import random
from src.scripts.game_dir.game import Game


class ServerGameCoordinator:
	__words: dict

	def __init__(self, player, UI):
		with open("src/resources/jsons/words.json", "r", encoding="UTF-8") as words:
			self.__words = json.load(words)

		self.__theme = random.choice(list(self.__words.keys()))
		word = random.choice(self.__words[self.__theme])
		self.__game = Game(word)
		self.__player = player
		self.__gameUI = UI
		self.__player.send_message_to_client(bytes(word, "utf-8"))

	def handle_message_from_client(self):
		while True:
			data = self.__player.get_message_from_client()

			if self.__game.players_turn:
				self.__game.on_letter_use(data.decode("utf-8"))

				self.__game.change_players_turn()

	def send_message_to_clientGC(self, msg):
		self.__player.send_message_to_client(msg.encode("utf-8"))


class ClientGameCoordinator:
	def __init__(self, player, UI):
		self.__player = player
		self.__gameUI = UI
		word = self.__player.get_message_from_server()
		self.__game = Game(word)
		self.__game.change_players_turn()

	def handle_message_from_server(self):
		while True:
			data = self.__player.get_message_from_server()

			if not self.__game.players_turn:
				self.__game.on_letter_use(data.decode("utf-8"))

				self.__game.change_players_turn()

	def send_message_to_serverGC(self, msg):
		self.__player.send_message_to_server(msg.encode("utf-8"))





