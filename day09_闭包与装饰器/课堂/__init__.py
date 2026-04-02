

def func(a, b, c):
    print(a)
    print(b)
    print(c)

func(1, 2, 3)

tuple = (1, 2, 3)

func(*tuple)
print("------------------------------------------")
func(a = 4,  b = 5, c = 6)

dict = {"a": 4, "b": 5, "c": 6}

func(**dict)

def func2(*args, **kwargs):
    print(args)
    print(kwargs)

func2(1, 1, 3, 4, 5, a = 6, b = 7, c = 8)

# *是展开和收集元组的
# **是展开和收集字典的

# if __name__ == '__main__':
