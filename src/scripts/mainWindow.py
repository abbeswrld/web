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
		self.__indexes = [i for i in range(1, 21)]

	def index_to_string(self):
		return f"src/resources/images/{self.__index}.png"

	def __fill_index_array(self):
		self.__indexes = [i for i in range(1, 21)]

	@property
	def pixmap(self):
		return self._pixmap

	def __update_pixmap(self):
		self._pixmap = QPixmap(self.index_to_string())

	def update_image_index(self):
		self.__index = random.choice(self.__indexes)
		self.__indexes.remove(self.__index)
		self.__update_pixmap()
		if len(self.__indexes) == 0:
			self.__fill_index_array()


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
			self.__server = Server(self, self.get_input()[1])
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
			if name == "image":
				self.label.setText(self.__server.get_hostname())
				self.label_2.setText(str(self.__server.get_port()))
		except Exception as e:
			print(e)

	def update_image_pixmap(self):
		self.__image.update_image_index()
		self.image.setPixmap(self.__image.pixmap)

	def on_mainbutton_click(self):
		self.__client.send_message_to_server_to_change_image()


