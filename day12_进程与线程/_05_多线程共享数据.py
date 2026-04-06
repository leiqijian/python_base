import threading
import time

num = 0

def sum1():
    print("sum1抢到了")
    time.sleep(5)
    global num
    for i in range(100_0000):
        num += 1
    print("sum1:", num)

def sum2():
    print("sum2抢到了")
    global num
    for i in range(100_0000):
        num += 1
    print("sum2:", num)

if __name__ == '__main__':
    thread1 = threading.Thread(target=sum1)
    thread2 = threading.Thread(target=sum2)
    thread1.start()
    thread2.start()
