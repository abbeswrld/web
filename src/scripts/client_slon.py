import socket

client = socket.socket()
hostname = socket.gethostname()
port = 1234
client.connect((hostname, port))
data = client.send("qwe".encode())

