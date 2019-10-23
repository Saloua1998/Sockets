import socket

# AF_INET = IPv4 and SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind a tuple of IP and Port
s.bind((socket.gethostname(), 1234))
# server will listen for messages/connections
# it has a queue of 5
s.listen(5)

while True:
    # store the clientsocket object in clientsocket
    # store the client IP address in address
    clientsocket, address = s.accept()

    print(f"Connection from {address} has been established!")
