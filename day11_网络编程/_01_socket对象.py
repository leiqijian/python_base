import socket

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

print(sock)
print(sock.connect_ex(('127.0.0.1', 8080)))