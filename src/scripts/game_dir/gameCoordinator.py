import json
import random
from src.scripts.game_dir.game import Game


class GameCoordinator:
	__words: dict

	def __init__(self, server, UI):
		with open("src/resources/jsons/words.json", "r", encoding="UTF-8") as words:
			self.__words = json.load(words)

		self.__theme = random.choice(list(self.__words.keys()))
		word = random.choice(self.__words[self.__theme])
		self.__game = Game(word)
		self.__server = server
		self.__gameUI = UI




