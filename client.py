import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))
print("Connected to the server")

while True:
    server_message = client_socket.recv(1024).decode()
    print("Received message: ", server_message)

client_socket.close()