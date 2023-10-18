import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "192.168.1.22"
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


# The pickle module could be used to send objects instead of strings.
def send(msg):
    message = msg.encode(FORMAT)
    # For some reason we have to send a byte string first with the integer size of the message, concatenated with spaces
    # until it hits the length of the header.
    send_length = str(len(message)).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    message_ = input('Message: ')
    send(message_)
    if message_ == "!DISCONNECT":
        break