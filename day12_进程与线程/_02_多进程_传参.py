import time
import multiprocessing, os

def coding(name, num):
    print(os.getpid())
    print(multiprocessing.current_process().pid)
    print("------")
    print(os.getppid())
    print(multiprocessing.parent_process().pid)
    for i in range(num):
        print(f"{name}正在敲第{i+ 1}行代码")
        # time.sleep(0.01)

def drawing(name, num):
    for i in range(num):
        print(f"{name}正在画第{i + 1}笔画")
        # time.sleep(0.01)

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=coding, args=("leimen", 100))
    p2 = multiprocessing.Process(target=drawing, args=("Jenny", 20))

    p1.start()
    # p2.start()
