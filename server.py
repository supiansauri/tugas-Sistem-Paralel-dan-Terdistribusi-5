# server.py
# Importing neccessary inbuilt modules
import socket
import random
import string

# Creating a socket instance
server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connecting to the localhost
ip_address = '127.0.0.1'
port = 5555
server_object.bind((ip_address, port))
server_object.listen()

print("Menunggu koneksi dengan client")

#Once the client connects to the particular port, the server starts to accept the request.
connection_object, _ = server_object.accept()

if connection_object:
	# Connected to client successfully
    print("Terkoneksi dengan client\n")
    
    # sending initial message to the client
    connection_object.send(b"SERVER: hallo! silahkan kirim pesan, atau kirim 'stop' untuk memutuskan koneksi")
    
    # receiving message from the client
    data_receive = connection_object.recv(1024)
    
    while data_receive != b'stop':
        client_message = data_receive.decode('utf-8')
        print(f"CLIENT: {client_message}")

        server_input = input("SERVER: ").encode('utf-8')
        connection_object.send(server_input)

        data_receive = connection_object.recv(1024)