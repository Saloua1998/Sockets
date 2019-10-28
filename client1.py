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
    data = {"studentnr": input("studentnr: "), "classname": input("classname: "), "clientid": int(input("clientid: ")), "teamname": input("teamname: "), "ip": input("ip: "), "secret": None, "status": None}
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
                        msg = json.loads(msg)
                        connectServerAgain()
                        updatemsg = msg.update({"studentnr": input("studentnr: "), "clientid": int(input("clientid: ")), "ip": input("ip: ")})
                        d = json.dumps(updatemsg)
                        s.send(bytes(d, "utf-8"))
                        print("done")
                        print(msg) #{'studentnr': '0965662', 'classname': '1', 'clientid': 2, 'teamname': '1', 'ip': '145.137.11.122', 'secret': '75d219755a6a9e84656a5a8cb6b5177a8d61a1a25e5378831db9ef5e575c00f3', 'status': 'waiting for message 2'}
                        print(updatemsg) #None
                        print(d) #null
                        break

            


            #--

        # if type(json.loads(msg)) == 'dict':
        # print(type(json.loads(msg)))
        # print("Type: ", type(json.loads(msg)))
