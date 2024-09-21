import socket


class Server:
    def __init__(self, hostname="mamin_papa_ded", port=1234):
        self.__socket = socket.socket()
        self.__hostname = hostname
        self.__port = port
        self.__connection = None
        self.__client_address = None

    def start_server_listen(self):
        try:
            self.__socket.bind((self.__hostname, self.__port))
            self.__socket.listen(1)
            self.__connection, self.__client_address = self.__socket.accept()
            return "successfully"
        except Exception as e:
            return str(e)

    def handle_message_from_client(self):
        while True:
            data = self.__connection.recv(1024)
            if not data:
                break
            print(data.decode())

    def close_connection_with_client(self):
        self.__connection.close()
        self.__connection = None


s = Server()
s.start_server_listen()
s.handle_message_from_client()
