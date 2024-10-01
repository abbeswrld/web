from PyQt5 import uic, Qt, QtCore
from PyQt5.QtWidgets import QMainWindow
from ui_constants import *
import pictures



class GameWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(UI_DIR + "5word.ui", self)
		self.who_win.hide()

		self.all_btns = self.findChildren(Qt.QPushButton)

		self.btns = [btn for btn in self.all_btns if not btn.objectName().startswith("let_")]
		self.btns_let = [btn for btn in self.all_btns if btn.objectName().startswith("let_")]

		for btn in self.btns_let:
			btn.setStyleSheet("""
				QPushButton:disabled{
					background-color:rgba(255, 255, 255, 0);
					color: rgb(0, 0, 0);
					font: 19pt 'MS Shell Dlg 2' bold;
				}
			""")

		for btn in self.btns:
			btn.setStyleSheet("""
				QPushButton {
					background-color: rgb(206, 246, 255, 0);
					border-radius: 20px;
					border: 4px solid rgb(40, 40, 40);
					color: rgb(79, 76, 62);
					font: 16pt 'Segoe Print' ; 
				}

				QPushButton:hover {
					background-color: rgb(206, 246, 255, 40);
					border-radius: 20px;
					color: rgb(79, 76, 62);
					border: 3px solid rgb(40, 40, 40);
					font: 18pt 'Segoe Print' ; 
				}
				""")

	def end_game(self, who_win: bool):
		self.who_win.show()
		self.who_win.setText("Вы победили!" if who_win else "Друг победил(")

	def update_turn(self, which_turn):
		if which_turn:
			self.your_turn.setStyleSheet("""
			QPushButton {
				background-color: rgb(255, 7, 127);
				alternate-background-color: rgb(184, 0, 31);
				color:rgb(20, 20, 20);
				border-radius: 10px;
				border: 4px solid rgb(255, 40, 130)
			}
			""")
			self.your_turn.setText("Не ваш ход")
		else:
			self.your_turn.setStyleSheet("""
			QPushButton {
				background-color: rgb(110, 194, 7);
				alternate-background-color: rgb(184, 0, 31);
				color:rgb(245, 245, 245);
				border-radius: 10px;
				border: 4px solid rgb(110, 194, 100)
			}
			""")
			self.your_turn.setText("ваш ход")
