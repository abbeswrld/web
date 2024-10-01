from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_constants import *


class ClientWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(UI_DIR + "enter.ui", self)

	def get_entered_hostname(self):
		try:
			return self.enter_host.text()
		except Exception as e:
			print(e)
			return "mamin_papa_ded"

	def get_entered_port(self):
		try:
			return int(self.enter_port.text())
		except Exception as e:
			print(e)
			return 9090

	def closeEvent(self, event):
		QApplication.quit()
		event.accept()