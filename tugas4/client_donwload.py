import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)

requestfile = "2.png"
request = "download "+requestfile
sock.send(request.encode('utf-8'))
sock.shutdown(socket.SHUT_WR)
#print(request)

data = sock.recv(1024)
if data == b'File not exist':
    print("File not exist")
else:
    f = open("Client/"+requestfile,"wb")
    while (data):
        print(data)
        f.write(data)
        data = sock.recv(1024)
        #f = open("Server/2.png", "rb")
        #print(f.read())
        # print(base64.decode(data))
    print("file " + requestfile + " has been downloaded")
    f.close()


print("Close . . .")
sock.close()