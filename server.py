import socket
import threading

PORT = 5050
# SERVER = '192.168.0.30'
# Change this to the public IP address to allow access across multiple networks
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
HEADER = 64  # The number of bytes expected to get from the client
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# AF_INET is the type of addresses we are looking for
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address} connected.")

    while True:
        # This line also blocks until it receives a message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                conn.close()
                break

            print(f'[{address}] {msg}')
            conn.send("Message Received".encode(FORMAT))


def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}.')
    while True:
        # This line will wait until it finds a connection.
        conn, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}.")


print("[STARTING] Server is starting...")
start()
