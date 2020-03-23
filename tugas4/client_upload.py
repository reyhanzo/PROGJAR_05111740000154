import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = "2.png"
if os.path.isfile("Client/" + Filename):
    Send = "upload " + Filename
    print("Sending: " + Filename)
    myfile = open("Client/" + Filename, "rb")
    Filename = "ASD" + Send
    Fil8 = Filename.encode("utf-8")
    datasend = myfile.read() + Fil8
    sock.send(datasend)
    sock.shutdown(socket.SHUT_WR)
    hasil = sock.recv(10).decode()
    print(hasil)
else:
    print("File not Exist")

print("Closing")
sock.close()