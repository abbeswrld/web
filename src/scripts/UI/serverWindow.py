from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_constants import *


class ServerWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.closed = QtCore.pyqtSignal(str)
		uic.loadUi(UI_DIR + "waiting.ui", self)
		self.setWindowIcon(QtGui.QIcon(IMAGE_DIR + 'kubik.png'))


	def set_label_hostname(self, hostname: str):
		self.s_host.setText(hostname)

	def set_label_port(self, port: int):
		try:
			port = str(port)
		except Exception as e:
			port = "5050"
			print(e)
		self.s_port.setText(port)

	def closeEvent(self, event):
		QApplication.quit()
		event.accept()
