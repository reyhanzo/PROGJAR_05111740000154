import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 31003)
print(f"starting up on {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

i = 1

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")

    # Receive file
    file = open('file_'+ str(i)+".pdf",'wb') # Open in binary
    i = i + 1

    while True:
        data = connection.recv(1024)
        # print(sys.stderr, 'received ', data)
        while(data):
            file.write(data)
            data = connection.recv(1024)
    file.close()

    # Clean up the connection
    connection.close()