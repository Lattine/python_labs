# -*- coding: utf-8 -*-

# @Time    : 2019/11/20
# @Author  : Lattine

# ======================
from datetime import datetime
import socket

HOST = "127.0.0.1"
PORT = 12345
BUF_SIZE = 1024
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
while True:
    print(f"waiting for client...")
    client_socket, addr = server.accept()
    print(f"... connecting from : {addr}")

    while True:
        data = client_socket.recv(BUF_SIZE)
        if not data:
            break
        client_socket.send(f"{datetime.now()}, {data}".encode("utf-8"))
    client_socket.close()

server.close()
