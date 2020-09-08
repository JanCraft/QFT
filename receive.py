import socket

HOST = input("Host: ")
PORT = 5566

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    fname = data.decode('utf-8')
    input("Press enter to start the reception of '" + fname + "'")
    s.send(bytes(1))
    data = s.recv(1024)
    amnt = int(data.decode('utf-8'))
    file = open(fname, 'wb')
    data = s.recv(amnt)
    file.write(data)
    file.close()
