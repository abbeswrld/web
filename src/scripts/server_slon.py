import socket
import threading
from src.scripts.game_dir.gameCoordinator import GameCoordinator
from src.scripts.UI.gameWindow import GameWindow


class Server:
    def __init__(self, serverUI):
        self.__server_UI = serverUI
        self.__socket = socket.socket()
        self.__hostname = socket.gethostname()
        self.__port = 5050
        self.__connection = None
        self.__thread = None
        self.__server_UI.set_label_hostname(self.__hostname)
        self.__server_UI.set_label_port(self.__port)

    def start_server_thread(self):
        self.__thread = threading.Thread(target=self.__start_listen)
        self.__thread.start()

    def __start_listen(self):
        try:
            self.__socket.bind((self.__hostname, self.__port))
            self.__socket.listen(1)
            self.__connection, current_address = self.__socket.accept()
            gw = GameWindow()
            gw.show()

            self.__server_UI.destroy()
        except Exception as e:
            print(str(e))
            return str(e)

    def handle_message_from_client(self):
        return self.__connection.recv(1024)

    def send_message_to_client(self, msg):
        self.__connection.send(msg)

    def get_hostname(self):
        return self.__hostname

    def get_port(self):
        return self.__port