import socket
import time

def connect_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(sock)

    # sock.connect(('192.168.66.122', 12306))
    sock.connect(('127.0.0.1', 12306))
    # sock.connect(('', 10086))
    while True:
        str = input("我说")
        if str == 'exit':
            sock.close()
            break
        sock.send(str.encode(encoding='utf-8'))
        receive_data = sock.recv(1024)
        print(receive_data.decode())

if __name__ == '__main__':
    # while True:
        connect_socket()
        # time.sleep(2)