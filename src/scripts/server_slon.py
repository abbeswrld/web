import socket
import threading


class Server:
    def __init__(self, serverUI, hostname, port):
        self.__server_UI = serverUI
        self.__socket = socket.socket()
        self.__hostname = hostname if hostname else "mamin_papa_ded"
        self.__port = port if port else 1234
        self.__connection = None
        self.__client_addresses = []
        self.__thread = None

    def start_server_thread(self):
        self.__thread = threading.Thread(target=self.__start_listen)
        self.__thread.start()

    def __start_listen(self):
        try:
            self.__socket.bind((self.__hostname, self.__port))
            self.__socket.listen(1)
            self.__connection, current_address = self.__socket.accept()
            while self.__connection:
                self.handle_message_from_client()
        except Exception as e:
            print(str(e))
            return str(e)

    def handle_message_from_client(self):
        while True:
            data = self.__connection.recv(1024)
            if not data:
                break
            if data.decode() == "change_image":
                self.__server_UI.update_image_pixmap()

    def close_connection_with_client(self):
        self.__connection.close()
        self.__connection = None