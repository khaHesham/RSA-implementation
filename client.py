import socket
import RSA as RSA

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect(('localhost', 8000))

# send data to the server
public_B,private_B = RSA.generate_keys(64)
client_socket.send(str(public_B[0]).encode())  # send n
client_socket.send(str(public_B[1]).encode())  # send e


# receive a response from the server
public_A = (int(client_socket.recv(1024).decode()),int(client_socket.recv(1024).decode()))
print(f"Received pub-key from server: {public_A}")

while True:
    # recieve number of groups
    n_blocks=int(client_socket.recv(1024).decode())

    # recieve data
    de=[]
    for i in range(n_blocks):
        encoded = int(client_socket.recv(1024).decode())
        de.append(RSA.decrypt(encoded, private_B))
        # messageReceived += RSA.en.decode(RSA.decrypt(encoded, private_B))

    messageReceived = RSA.en.decode(de)
    print(f"Received message from server : {messageReceived}")


    # send data
    message=input("please write a message to send to server : ")
    encoded_messages=RSA.en.encode(message)

    # send number of groups
    client_socket.send(str(len(encoded_messages)).encode())

    # send message
    for encoded in encoded_messages:
        enc = RSA.encrypt(int(encoded),public_A)
        # send a response to the client
        client_socket.send(str(enc).encode())

    
# close the connection
client_socket.close()
