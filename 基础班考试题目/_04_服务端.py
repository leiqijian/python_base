# 题目：使用套接字编程完成TCP客户端开发，连接服务器地址：192.168.108.88，端口号为8000，客户端主动向服务器端发送文本"hello，itheima"，并接受服务器端返回结果。

import socket

def server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('192.168.108.88', 8000))

    server.listen(5)

    connect_socket, client_info = server.accept()

    data = connect_socket.recv(1024).decode("utf-8")
    print(data)

    connect_socket.close()

if __name__ == '__main__':
    server()