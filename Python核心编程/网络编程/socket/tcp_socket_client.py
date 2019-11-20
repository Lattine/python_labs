# -*- coding: utf-8 -*-

# @Time    : 2019/11/20
# @Author  : Lattine

# ======================
import socket

HOST = "127.0.0.1"
PORT = 12345
BUF_SIZE = 1024
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    data = input(">")
    if not data:
        break
    client.send(data.encode("utf-8"))
    data = client.recv(BUF_SIZE)
    if not data:
        break
    print(data.decode("utf-8"))
client.close()
