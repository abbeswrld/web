import socket

client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост сервера
port = 14337  # устанавливаем порт сервера
client.connect((hostname, port))  # подключаемся к серверу
data = client.recv(1024)  # получаем данные с сервера
while True:
    a = input()
    if a == "x":
        print("Server sent: ", data.decode())  # выводим данные на консоль
    elif a == "end":
        client.close()
        break
