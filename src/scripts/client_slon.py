import socket


class Client:
	def __init__(self, client_UI):
		self.__client_UI = client_UI
		self.__socket = socket.socket()
		self.__client_UI.button_confirm.clicked.connect(self.connect_to_server)

	def connect_to_server(self):
		hostname = self.__client_UI.get_entered_hostname()
		port = self.__client_UI.get_entered_port()
		hostname = hostname if hostname else "mamin_papa_ded"
		try:
			self.__socket.connect((hostname, port))
			return True
		except:
			return False

	def send_message_to_server(self, msg):
		self.__socket.send(msg.encode())

	def handle_message_from_server(self):
		return self.__socket.recv(1024)
