from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from ui_constants import *


class ClientWindow(QDialog):
	def __init__(self):
		super().__init__()
		uic.loadUi(UI_DIR + "enter.ui", self)

	def get_entered_hostname(self):
		return self.enter_host.getText()

	def get_entered_port(self):
		try:
			return int(self.enter_port.getText())
		except Exception as e:
			print(e)
			return 5050