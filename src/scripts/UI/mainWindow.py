from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from src.scripts.server_slon import Server
from src.scripts.client_slon import Client
from src.scripts.UI.serverWindow import ServerWindow
from src.scripts.UI.clientWindow import ClientWindow
from ui_constants import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(UI_DIR + "choice.ui", self)
		self.create_server_btn.clicked.connect(self.on_create_host_button_click)
		self.find_server_btn.clicked.connect(self.on_find_host_button_click)

	def on_create_host_button_click(self):
		try:
			server_ui = ServerWindow()
			server_ui.show()
			self.__server = Server(server_ui)
			self.destroy()
		except Exception as e:
			print(e)

	def on_find_host_button_click(self):
		client_ui = ClientWindow()
		client_ui.show()
		self.__client = Client(client_ui)
		self.destroy()




