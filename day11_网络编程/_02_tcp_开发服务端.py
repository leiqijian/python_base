import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# sock.bind(('192.168.66.122', 12306))
sock.bind(('', 12306))

sock.listen(500)

while True:
    try:
        connect_socket, client_socket = sock.accept()

        connect_socket.send(b'I have received a message')

        data = connect_socket.recv(1024).decode("utf-8")
        if data == 'exit':
            connect_socket.close()
            break
        print(data)

    except Exception as e:
        print(e)

