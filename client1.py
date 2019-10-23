import socket

# AF_INET = IPv4 and SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server IP and port
s.connect((socket.gethostname(), 1234))

while True:
    # 8 is the buffersize
    msg = s.recv(1000)
    # decode the received message and print it out
    print(msg.decode("utf-8"))
