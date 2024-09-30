from PyQt5 import uic, Qt, QtCore
from PyQt5.QtWidgets import QMainWindow
from ui_constants import *
import pictures



class GameWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(UI_DIR + "5word.ui", self)
		self.all_btns = self.findChildren(Qt.QPushButton)

		self.btns = [btn for btn in self.all_btns if not btn.objectName().startswith("let_")]
		self.btns_let = [btn for btn in self.all_btns if btn.objectName().startswith("let_")]

		print([btn.objectName() for btn in self.btns_let])

		for btn in self.btns_let:
			btn.setEnabled(False)

	def end_game(self, who_win: bool):
		self.who_win.enable()
		self.who_win.setText("Вы победили!" if who_win else "Друг победил(")

	def update_turn(self, which_turn):
		if which_turn:
			self.your_turn.setStyleSheet("background-color:red")  # TODO alternative-background-color
			self.your_turn.setText("Не ваш ход")
		else:
			self.your_turn.setStyleSheet("background-color:green")
			self.your_turn.setText("ваш ход")
