from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from ui_constants import *


class GameWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(UI_DIR + "5word.ui", self)
		