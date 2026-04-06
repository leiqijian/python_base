import time
import multiprocessing

def coding():
    for i in range(1000):
        print("正在敲第{}行代码".format(i))
        # time.sleep(0.01)

def drawing():
    for i in range(1000):
        print("正在画第{}笔画".format(i))
        # time.sleep(0.01)

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=drawing)

    p1.start()
    p2.start()
