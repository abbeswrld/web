from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from src.scripts.server_slon import Server
from src.scripts.client_slon import Client


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("src/resources/UI/main_v2.ui", self)
		self.__pages = {
			"main": 0,
			"button": 1,
			"image": 2
		}
		self.create_server_btn.clicked.connect(self.on_create_host_button_click)
		self.find_server_btn.clicked.connect(self.on_find_host_button_click)

	def on_create_host_button_click(self):
		try:
			self.server = Server(*self.get_input())
			self.server.start_server_thread()
			self.translate_ui("image")
		except Exception as e:
			print(e)

	def on_find_host_button_click(self):
		try:
			self.client = Client()
			print(self.get_input())
			self.client.connect_to_server(*self.get_input())
			self.translate_ui("button")
		except Exception as e:
			print(e)
	def get_input(self):
		return [self.hostname_input.text(), self.port_input.text()]

	def translate_ui(self, name: str):
		try:
			self.stacked.setCurrentIndex(self.__pages[name])
		except Exception as e:
			print(e)

	def



