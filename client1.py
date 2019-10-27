import socket
import json

# AF_INET = IPv4 and SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server IP and port
connect = s.connect(('145.24.222.103', 8001))

nameClient = input("client 1 or 2? ")


def sendObject():
    if(nameClient=="1"):
        data = {"studentnr": input("studentnr: "), "classname": input("classname: "), "clientid": 1, "teamname": input("teamname: "), "ip":input("ip: "), "secret": None, "status": None}
        d = json.dumps(data)
        s.send(bytes(d, "utf-8"))

    else: pass



while True:

    # 8 is the buffersize
    msg = s.recv(1000)
    # decode the received message and print it out
    print(msg.decode("utf-8"))

    sendObject()
    
    

    

    
