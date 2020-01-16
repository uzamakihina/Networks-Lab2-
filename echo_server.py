import socket, time
from multiprocessing import Process

HOST = ""
port = 8001
BUFFER_SIZE = 1024

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST,port))


        s.listen(2)
        while True:
            conn, addr = s.accept()
            print("connected by ", addr)
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            time.sleep(0.5)
            conn.sendall(bytearray(full_data))
            conn.close()


main()
