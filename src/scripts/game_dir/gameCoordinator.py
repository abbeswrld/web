import json
import random

from PyQt5 import QtCore
from src.scripts.game_dir.game import Game

from useful_func import create_and_start_thread


class ServerGameCoordinator:

	def __init__(self, player, UI):
		with open("src/resources/jsons/words.json", "r", encoding="UTF-8") as words:
			self.__words = json.load(words)

		self.__theme = random.choice(list(self.__words.keys()))
		word = random.choice(self.__words[self.__theme])
		self.__game = Game(word)
		self.__player = player
		self.__gameUI = UI

		self.__gameUI.setWindowTitle("server")

		self.__player.send_message_to_client(bytes(word, "utf-8"))

		for btn in self.__gameUI.btns:
			btn.clicked.connect(self.on_button_click)

		create_and_start_thread(self.handle_message_from_client)


	def handle_message_from_client(self):
		while True:
			data = self.__player.get_message_from_client().decode("utf-8")
			print(data, 123)
			if len(data) == 1:
				if self.__game.players_turn:
					btn = self.find_button_by_text(data)
					btn.setEnabled(False)

					if not self.update_answer_btns(data):
						self.__game.change_players_turn()

			else:
				if data == "end":
					self.__gameUI.end_game(False)

	def send_message_to_clientGC(self, msg):
		self.__player.send_message_to_client(msg.encode("utf-8"))

	def on_button_click(self):
		print(2)
		print(self.__game.players_turn)
		btn = self.__gameUI.sender()
		if not self.__game.players_turn:
			btn.setEnabled(False)
			letter = btn.text()

			self.__game.on_letter_use(letter)
			if not self.update_answer_btns(letter):
				self.__game.change_players_turn()

			self.send_message_to_clientGC(letter)

			if self.__game.check_win():
				self.__gameUI.end_game(True)

				self.send_message_to_clientGC("end")

	def find_button_by_text(self, text):
		for btn in self.__gameUI.btns:
			if btn.text() == text:
				return btn

	def update_answer_btns(self, let):
		if let in self.__game.word:
			index_of_answer_letter = self.__game.word.index(let)
			self.__gameUI.btns_let[index_of_answer_letter].setText(let)
			return True
		return False

class ClientGameCoordinator:
	def __init__(self, player, UI):
		self.__player = player
		self.__gameUI = UI
		word = self.__player.get_message_from_server().decode("utf-8")
		self.__game = Game(word)

		self.__gameUI.setWindowTitle("client")

		create_and_start_thread(self.handle_message_from_server)

		for btn in self.__gameUI.btns:
			btn.clicked.connect(self.on_button_click)

	def handle_message_from_server(self):
		while True:
			data = self.__player.get_message_from_server().decode("utf-8")
			if len(data) == 1:
				if not self.__game.players_turn:
					btn = self.find_button_by_text(data)
					btn.setEnabled(False)

					self.__game.on_letter_use(data)
					if not self.update_answer_btns(data):
						self.__game.change_players_turn()

			else:
				if data == "end":
					self.__gameUI.end_game(False)

	def send_message_to_serverGC(self, msg):
		self.__player.send_message_to_server(msg.encode("utf-8"))

	def on_button_click(self):
		print(3)
		print(self.__game.players_turn)
		btn = self.__gameUI.sender()
		if self.__game.players_turn:
			btn.setEnabled(False)
			letter = btn.text()

			self.__game.on_letter_use(letter)
			if not self.update_answer_btns(letter):
				self.__game.change_players_turn()

			try:
				self.send_message_to_serverGC(letter)
			except Exception as e:
				print(e)

			if self.__game.check_win():
				self.__gameUI.end_game(True)

	def find_button_by_text(self, text):
		for btn in self.__gameUI.btns:
			if btn.text() == text:
				return btn

	def update_answer_btns(self, let):
		if let in self.__game.word:
			print("smth")
			index_of_answer_letter = self.__game.word.index(let)
			self.__gameUI.btns_let[index_of_answer_letter].setText(let)
			return True
		return False




