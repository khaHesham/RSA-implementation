import socket
import RSA as RSA

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port
server_socket.bind(('localhost', 8000))

# set the socket to listen for incoming connections
server_socket.listen()

print("Server is listening for incoming connections...")

# accept the client connection
client_socket, address = server_socket.accept()

print(f"Connection established from {address}")

# receive data from the client
public_B = (int(client_socket.recv(1024).decode()),int(client_socket.recv(1024).decode()))
print(f"Received pub-key from client: {public_B}")

# send server public key
public_A,private_A = RSA.generate_keys(64)
client_socket.send(str(public_A[0]).encode())  # send n
client_socket.send(str(public_A[1]).encode())  # send e

# handshake is done now get the message and encrypt it



while True:
    # get the message
    message=input("please write a message to send : ")
    encoded_messages=RSA.en.encode(message)

    # send number of groups
    client_socket.send(str(len(encoded_messages)).encode())

    # send message
    for encoded in encoded_messages:
        enc = RSA.encrypt(int(encoded),public_B)
        # send a response to the client
        client_socket.send(str(enc).encode())


    # recieve number of groups
    n_blocks=int(client_socket.recv(1024).decode())

    # recieve data
    de=[]
    for i in range(n_blocks):
        encoded = int(client_socket.recv(1024).decode())
        de.append(RSA.decrypt(encoded, private_A))
        # messageReceived += RSA.en.decode(RSA.decrypt(encoded, private_B))

    messageReceived = RSA.en.decode(de)
    print(f"Received message from client : {messageReceived}")




    


# close the connection
client_socket.close()
server_socket.close()
