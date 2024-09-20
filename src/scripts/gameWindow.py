from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class GameWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("src/resources/UI/game.ui", self)
