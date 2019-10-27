import socket
import json

# AF_INET = IPv4 and SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server IP and port
connect = s.connect(('145.24.222.103', 8001))

nameClient = input("client 1 or 2? ")


def sendObject():
    if(nameClient == "1"):
        data = {"studentnr": input("studentnr: "), "classname": input("classname: "), "clientid": 1, "teamname": input(
            "teamname: "), "ip": input("ip: "), "secret": None, "status": None}
        d = json.dumps(data)
        s.send(bytes(d, "utf-8"))
    else:
        pass


sendObject()

while True:
    # 1000 is the buffersize
    msg = s.recv(1000).decode("utf-8")
    # decode the received message and print it out
    if msg.startswith('{'):
        status = json.loads(msg)["status"]
        print(status)
        # If status == "waiting for message 2" than send to server
        if status == "waiting for message 2":

            s.send(bytes(msg, "utf-8"))
        else:
            s.send(bytes(msg, "utf-8"))
    else:
        print(msg)

        # if type(json.loads(msg)) == 'dict':
        # print(type(json.loads(msg)))
        # print("Type: ", type(json.loads(msg)))
