import socket


class Client:
	def __init__(self):
		self.__socket = socket.socket()

	def connect_to_server(self, hostname="mamin_papa_ded", port=1234):
		self.__socket.connect((hostname, port))

	def send_message_to_server(self, message):
		message = message.encode() if type(message) is str else message
		print(self.__socket.send(message))


client = Client()
client.connect_to_server()
client.send_message_to_server("123")
