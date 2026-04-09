# 列举出所有的可能  有可能无效
# a: 0 1 2 3 4 5 6 1000
# b: 0 1 2 3 4 5 6 1000
# c: 0 1 2 3 4 5 6 1000
import time


def compute_time(fn):
    def wrapper():
        time_start = time.time()
        fn()
        time_end = time.time()
        print(f'一共运行多久: {time_end - time_start}')
    return wrapper

@compute_time
def func():
    for a in range(1001):
        for b in range(1001):
            # print(a, b) # 1001 * 1001
            for c in range(1001):
                # print(a, b, c) # 1001**3    1000**3 = 10_0000_0000
                # 49s
                # if a + b + c == 1000 and a**2 + b**2 == c**2 :
                if a**2 + b**2 == c**2 and a + b + c == 1000 :
                    print(a, b, c)

func()