import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    f = open("reyfile.pdf", "rb")
    l = f.read(102400)
    while (l):
        sock.send(l)
        l = f.read(102400)
finally:
    print(sys.stderr, 'closing socket')
    sock.close()