import socket
from src.scripts.game_dir.gameCoordinator import ServerGameCoordinator
from src.scripts.UI.gameWindow import GameWindow
from useful_func import create_and_start_thread


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
        create_and_start_thread(self.__start_listen)

    def __start_listen(self) -> None:
        try:
            self.__socket.bind((self.__hostname, self.__port))
            self.__socket.listen(1)
            self.__connection, current_address = self.__socket.accept()
            if self.__connection:
                self.on_connect()
            self.__server_UI.destroy()
        except Exception as e:
            print(str(e))

    def on_connect(self) -> None:
        gw = GameWindow()
        gw.show()
        ServerGameCoordinator(self, gw)

    def handle_message_from_client(self) -> bytes:
        return self.__connection.recv(1024)

    def send_message_to_client(self, msg: bytes) -> None:
        self.__connection.send(msg)

    def get_hostname(self) -> str:
        return self.__hostname

    def get_port(self) -> int:
        return self.__port