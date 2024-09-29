from PyQt5 import uic, Qt, QtCore
from PyQt5.QtWidgets import QMainWindow
from ui_constants import *


class GameWindow(QMainWindow):
	on_letter_button_clicked_signal = QtCore.pyqtSignal(object)

	def __init__(self):
		super().__init__()
		uic.loadUi(UI_DIR + "5word.ui", self)
		self.all_btns = self.findChildren(Qt.QPushButton)

		self.btns = [btn for btn in self.all_btns if not btn.objectName().startswith("let_")]
		self.btns_let = [btn for btn in self.all_btns if btn.objectName().startswith("let_")]

		for btn in self.btns_let:
			btn.setEnabled(False)

		for btn in self.btns:
			btn.clicked.connect(self.on_click)

	def on_click(self):
		print("123")
		self.on_letter_button_clicked_signal.emit(self.sender().text())

		print(self.sender().text())

	def end_game(self, who_win: bool):
		self.who_win.setText("Вы победили!" if who_win else "Друг победил(")