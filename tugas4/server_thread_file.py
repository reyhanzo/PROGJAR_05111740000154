from socket import *
import socket
import threading
import logging
import time
import sys

from file_machine import FileMachine

pm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = b''
            while True:
                datas = self.connection.recv(100)
                if not datas:
                    break
                data += datas
            if data:
                dd = b'a'
                if (len(data.split(b'ASD', 1)) == 2):
                    dd, data = data.split(b'ASD', 1)
                d = data.decode()
                cstring = d.split(" ")
                command = cstring[0].strip()
                hasil = pm.proses(d, dd)
                if (command == "download"): #download file
                    self.connection.sendall(hasil)
                if (command == "list"): # list file
                    self.connection.sendall(hasil.encode())
                if (command == "upload"): # upload file
                    self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8889))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    print("Running server . . .")
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()
