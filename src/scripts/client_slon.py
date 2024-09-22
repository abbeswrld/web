import socket


class Client:
	def __init__(self, client_UI):
		self.__client_UI = client_UI
		self.__socket = socket.socket()

	def connect_to_server(self, hostname, port):
		hostname = hostname if hostname else "mamin_papa_ded"
		port = int(port) if port else 1234
		try:
			self.__socket.connect((hostname, port))
			return True
		except:
			return False

	def send_message_to_server_to_change_image(self):
		self.__socket.send("change_image".encode())
