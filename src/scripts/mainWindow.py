from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("src/resources/UI/main_v2.ui", self)
