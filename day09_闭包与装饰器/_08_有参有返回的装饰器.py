#定义一个有参数有返回值的装饰器
def print_info(fn):
    def inner(x ,y): #嵌套函数，带有参数
        print("努力计算中")  # 额外功能
        return fn(x, y) #引用原函数，并把参数赋值给原函数
    return inner

#定义函数
@print_info
def func(x ,y):
    z = x + y
    return z

#调用函数
print(func(10, 20))
