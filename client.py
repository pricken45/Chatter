import socket
import threading

class Client:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.server.connect(('192.168.0.60', 9586))

        self.server.send(bytes("Hello", 'utf-8'))


cl = Client()
