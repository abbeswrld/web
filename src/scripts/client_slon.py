import socket


class Client:
	def __init__(self):
		self.__socket = socket.socket()

	def connect_to_server(self, hostname="mamin_papa_ded", port=1234):
		try:
			self.__socket.connect((hostname, port))
			return hostname, port
		except Exception as e:
			return str(e)

	def send_message_to_server(self, message):
		message = message.encode() if type(message) is str else message
		print(self.__socket.send(message))