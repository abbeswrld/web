import random
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from src.scripts.server_slon import Server
from src.scripts.client_slon import Client


class Image:
	def __init__(self):
		self.__index = 1  # an int num between 1 and 20
		self._pixmap = QPixmap(self.index_to_string())

	def index_to_string(self):
		return f"src/resources/images/{self.__index}.png"

	@property
	def pixmap(self):
		return self._pixmap

	def update_pixmap(self):
		self._pixmap = QPixmap(self.index_to_string())

	def update_image_index(self):
		self.__index = random.randint(1, 21)



class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("src/resources/UI/main_v2.ui", self)
		self.__image = Image()
		self.__pages = {
			"main": 0,
			"button": 1,
			"image": 2
		}
		self.create_server_btn.clicked.connect(self.on_create_host_button_click)
		self.find_server_btn.clicked.connect(self.on_find_host_button_click)
		self.mainbutton.clicked.connect(self.on_mainbutton_click)

	def on_create_host_button_click(self):
		try:
			self.__server = Server(self, *self.get_input())
			self.__server.start_server_thread()
			self.translate_ui("image")
		except Exception as e:
			print(e)

	def on_find_host_button_click(self):
		try:
			self.__client = Client(self)
			print(self.get_input())
			self.__client.connect_to_server(*self.get_input())
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

	def update_image_pixmap(self):
		self.__image.update_image_index()
		self.__image.update_pixmap()
		self.image.setPixmap(self.__image.pixmap)

	def on_mainbutton_click(self):
		self.__client.send_message_to_server_to_change_image()


