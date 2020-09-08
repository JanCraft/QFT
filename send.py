import socket, time

HOST = '0.0.0.0'
PORT = 5566

fname = input("Filename: ")
file = open(fname, 'rb')
data = file.read()
file.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening for QFT receiver...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.sendall(fname.encode('utf-8'))
        time.sleep(1)
        conn.recv(1)
        time.sleep(1)
        conn.sendall(str(len(data)).encode('utf-8'))
        time.sleep(1)
        conn.sendall(data)
        time.sleep(1)