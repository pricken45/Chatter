import socket
import threading


class Client:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    userName = input("Username: ")

    def sendMsg(self):
        while True:
            self.server.send(bytes(f"[{self.userName}] " + input(""), 'utf-8'))

    def __init__(self, ip, port):
        self.server.connect((ip, port))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()


        while True:
            data = self.server.recv(2048)

            if not data:
                break
            print(str(data, 'utf-8'))


client = Client(input('Ip: '), int(input('Port: ')))