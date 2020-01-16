import socket


addr = ('localhost', 8001)


cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(addr)
cli.send(bytearray("something",'utf-8'))

reply = cli.recv(4096)

cli.close()
print(reply)