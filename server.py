import socket
import threading


class Server:
    server: socket.socket = None
    connections = []

    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen(5)

    def handler(self, c, a):
        while True:
            data = c.recv(2048)

            for conn in self.connections:
                conn.send(data)
            if not data:
                self.connections.remove(c)
                break

    def run(self):
        while True:
            connection, address = self.server.accept()

            connThread = threading.Thread(target=self.handler, args=(connection, address))
            connThread.start()
            self.connections.append(connection)
            print(connection)


server = Server('Your ip', 2449)
server.run()
