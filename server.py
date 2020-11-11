import socket
import threading


class Server:
    server:socket.socket = None
    connections = []

    def __init__(self):
        print("Server is starting at 192.168.0.60:9586...")

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.bind(('192.168.0.60', 9586))
        self.server.listen(3)
        
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
            c, a = self.server.accept()

            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.start()
            
            self.connections.append(c)
            print(c)



server = Server()
server.run()

