

import socket


addr = ('www.google.com', 80)
payload ="GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(addr)
cli.send( bytearray( payload,'utf-8'))

reply = cli.recv(4096)

cli.close()

print(reply)




