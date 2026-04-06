import multiprocessing
import time


def fun():
     with open("E:\\github_project\\python_base\\day10_深浅拷贝_生成器_正则表达式\\data\\jaychou_lyrics.txt" ,encoding="utf-8") as f:
         data = f.readlines()
         print(data)


if __name__ == '__main__':
    start_time = time.time()
    fun()
    # multiprocessing.Process(target=fun).start()
    # multiprocessing.Process(target=fun).start()
    end_time = time.time()
    print(end_time - start_time)