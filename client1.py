import socket
import json

# AF_INET = IPv4 and SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server IP and port
s.connect(('145.24.222.103', 8001))

def connectServerAgain():
    # AF_INET = IPv4 and SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server IP and port
    s.connect(('145.24.222.103', 8001))

def sendObject():
    data = {"studentnr": input("studentnr: "), "classname": input("classname: "), "clientid": input("clientid: "), "teamname": input("teamname: "), "ip": input("ip: "), "secret": None, "status": None}
    d = json.dumps(data)
    s.send(bytes(d, "utf-8"))

def sendObjectFurther():
    # AF_INET = IPv4 and SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server IP and port
    s.connect((ipClient2, 1234))
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
            if (nameClient=="1"):
                ipClient2 = input("IP of client 2: ")
                sendObject()
            else: 
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind((socket.gethostname(), 1234))
                server.listen(5)
                while True:
                    # store the clientsocket object in clientsocket
                    # store the client IP address in address
                    clientsocket, address = server.accept()
                    # This is only a check to know is we're connected
                    msg = clientsocket.recv(1000)
                    msg = msg.decode("utf-8")
                    if msg:
                        print(msg)
                        updatemsg = msg
                        json.loads(updatemsg)["studentnr"] = input("studentnr: ")
                        json.loads(updatemsg)["clientid"] = input("clientid: ")
                        json.loads(updatemsg)["ip"] = input("ip: ")
                        connectServerAgain()
                        d = json.dumps(updatemsg)
                        s.send(bytes(d, "utf-8"))

            

            #--

        # if type(json.loads(msg)) == 'dict':
        # print(type(json.loads(msg)))
        # print("Type: ", type(json.loads(msg)))
