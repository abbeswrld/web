class Game:
	word: str
	available_letters = [chr(i) for i in range(ord("а"), ord("а") + 32)]
	used_letters: []
	players_turn = False
	is_game_ended = False

	def __init__(self, word):
		self.word = word

	def on_letter_use(self, letter: str):
		self.available_letters.remove(letter)
		self.used_letters.append(letter)

	def change_players_turn(self):
		self.players_turn = not self.players_turn
