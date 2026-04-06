import multiprocessing
import time


def work():
    for i in range(10):
        print("疯狂敲代码")
        time.sleep(0.2)

if __name__ == '__main__':
    print("主进程执行开始")
    p1 = multiprocessing.Process(target=work)

    #创建进程 设置为守护进程
    p1.daemon = True
    p1.start()
    time.sleep(1)

    print("主进程执行结束")
