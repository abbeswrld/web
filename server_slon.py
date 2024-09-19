import socket
from datetime import datetime

server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 14337  # устанавливаем порт сервера
server.bind((hostname, port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений

print("Server running")
while True:
    con, addr = server.accept()  # принимаем клиента
    print("client address: ", addr)
    message = datetime.now().strftime("%H:%M:%S")  # отправляем текущее время
    con.send(message.encode())  # отправляем сообщение клиенту
    con.close()  # закрываем подключение