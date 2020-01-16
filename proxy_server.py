



import socket, time
from multiprocessing import Process

HOST = ""
port = 8001
BUFFER_SIZE = 1024

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST,port))
        s.listen(1)
        while True:
            connect, address = s.accept()
            print("connected by ", address)
            time.sleep(0.5)

            addr = ('www.google.com', 80)
            payload ="GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

            cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cli.connect(addr)
            cli.send( bytearray( payload,'utf-8'))

            reply = cli.recv(4096)

            cli.close()

            connect.sendall(reply)
            connect.close()


main()
