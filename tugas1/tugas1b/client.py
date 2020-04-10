import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 31003)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = "derakkuma.png"
sock.send(Filename.encode('utf-8'))
sock.shutdown(socket.SHUT_WR)

f = open("reypicture_client.png", 'wb')  # open in binary
data = sock.recv(1024)
while(data):
    f.write(data)
    data = sock.recv(1024)
print("File received with namefile reypicture.png")
print("closing")
f.close()
sock.close()