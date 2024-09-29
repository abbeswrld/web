class Game:
	word: list
	bool_word: list
	players_turn: bool  # False - server's turn, True - client's turn.
	available_letters: list
	used_letters: list

	def __init__(self, word):
		self.word = list(word)
		self.reset()

	def on_letter_use(self, letter: str):
		self.available_letters.remove(letter)
		self.used_letters.append(letter)
		if letter in self.word:
			self.bool_word[self.word.index(letter)] = True

	def change_players_turn(self) -> bool:
		self.players_turn = not self.players_turn
		return self.players_turn

	def check_win(self) -> bool:
		return all(self.bool_word)

	def reset(self):
		self.word = []
		self.bool_word = [False] * 5
		self.players_turn = False
		self.available_letters = [chr(i) for i in range(ord("а"), ord("а") + 32)]
		self.used_letters = []
