###################################################
# Name:          Gizem Sazak     Saloua Oua-ali   #
# Studentnumber: 0965662         0958654          #
# Classname:     INF2D           INF2D            #
###################################################


import socket
import json

# AF_INET = IPv4 and SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the serverclient IP and port
s.connect(('145.24.222.103', 8001))

#it sends object to server
def sendObject():
    data = {"studentnr": input("studentnr: "), "classname": input("classname: "), "clientid": int(input("clientid: ")), "teamname": input("teamname: "), "ip": input("ip: "), "secret": None, "status": None}
    d = json.dumps(data)
    s.send(bytes(d, "utf-8"))

#it sends object to client 2
def sendObjectFurther(data):
    # AF_INET = IPv4 and SOCK_STREAM = TCP
    toClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the serverclient IP and port
    toClient.connect((ipClient2, 1234))
    toClient.send(bytes(data, "utf-8"))

def getIP():
    hostname = socket.gethostname() 
    ip = socket.gethostbyname(hostname)
    return ip 

client1=None
ipClient2 =""

nameClient = input("client 1 or 2? ")
print("Your IP: " + getIP())

while True:
    # 1000 is the buffersize
    msg = s.recv(1000)
    msg = msg.decode("utf-8")
    # decode the received message and print it out
    if msg:
       
        print(msg)
        if (msg.startswith('{') and client1==True):         
            sendObjectFurther(msg)
        else:
            if (nameClient=="1"):
                ipClient2 = input("IP of client 2: ")
                client1=True
                sendObject()
            else:
                client1=False
                #client 2 becomes server
                serverclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                serverclient.bind((socket.gethostname(), 1234))
                serverclient.listen(5)
                
                while True:
                    # store the clientsocket object in clientsocket
                    # store the client IP address in address
                    clientsocket, address = serverclient.accept()
                    # This is only a check to know is we're connected
                    msg = clientsocket.recv(1000)
                    msg = msg.decode("utf-8")
                    if msg:
                    #it sends to server incl server&secret     
                        print(msg)
                        msg = json.loads(msg)
                        msg.update({"studentnr": input("studentnr: "), "clientid": int(input("clientid: ")), "ip": input("ip: ")})
                        d = json.dumps(msg)
                        s.send(bytes(d, "utf-8"))
                        break
                        

            


 
