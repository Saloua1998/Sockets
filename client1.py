import socket
import json

# AF_INET = IPv4 and SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server IP and port
connect = s.connect(('145.24.222.103', 8001))

def sendObject():
    if(nameClient == "1"):
        data = {"studentnr": input("studentnr: "), "classname": input("classname: "), "clientid": 1, "teamname": input(
            "teamname: "), "ip": input("ip: "), "secret": None, "status": None}
        d = json.dumps(data)
        s.send(bytes(d, "utf-8"))
    else: pass

def sendObjectFurther():
    # AF_INET = IPv4 and SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server IP and port
    s.connect((ipClient2, 8001))
    s.send(bytes(newdata, "utf-8"))


while True:
    # 1000 is the buffersize
    msg = s.recv(1000)
    msg = msg.decode("utf-8")
    # decode the received message and print it out
    if msg:
        if msg.startswith('{'):
            status = json.loads(msg)["status"]
            print(msg)
            # If status == "waiting for message 2" than send to server
            if (status == 'waiting for message 2'):
             # s.send(bytes(status, "utf-8"))
             newdata = msg
             sendObjectFurther()
        else:
            print(msg)
            nameClient = input("client 1 or 2? ")
            text = "IP of client 2: "
            ipClient2 = input("")
            if(nameClient == "2"):
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind((socket.gethostname(), 8001))
                server.listen(5)
                while True:
                    # store the clientsocket object in clientsocket
                    # store the client IP address in address
                    clientsocket, address = server.accept()
                    # This is only a check to know is we're connected
                    msg = clientsocket.recv(1000)
                    msg = msg.decode("utf-8")
                    print(msg)
            else: sendObject()

        # if type(json.loads(msg)) == 'dict':
        # print(type(json.loads(msg)))
        # print("Type: ", type(json.loads(msg)))
