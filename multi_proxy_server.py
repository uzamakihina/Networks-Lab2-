
import socket, time ,sys
from multiprocessing import Process


HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    remote_ip = socket.gethostbyname(host)

    return remote_ip




def handle_request(conn,addr,proxy_end):
    send_full_data  =conn.recv(BUFFER_SIZE)

    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(BUFFER_SIZE)

    conn.send(data)

def main():

    host = 'www.google.com'
    port = 80
    

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")

        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        proxy_start.bind((HOST,PORT))

        proxy_start.listen(10)
        while True:
            conn, addr = proxy_start.accept()
            
            print("conneced by ", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("connecting to google")
                remote_ip = get_remote_ip(host)

                proxy_end.connect((remote_ip,port))

                p = Process(target=handle_request,args=(conn,addr,proxy_end))
                p.daemon = True 
                p.start()
                print("Started process ", p)

            conn.close()
main()
                
            
