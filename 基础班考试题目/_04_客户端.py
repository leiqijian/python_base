# 题目：使用套接字编程完成TCP客户端开发，连接服务器地址：192.168.108.88，端口号为8000，客户端主动向服务器端发送文本"hello，itheima"，并接受服务器端返回结果。

import socket

def client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('192.168.108.88', 8000))

    client.send("hello，itheima".encode("utf-8"))

    data = client.recv(1024).decode("utf-8")
    print(data)

    client.close()

if __name__ == '__main__':
    client()