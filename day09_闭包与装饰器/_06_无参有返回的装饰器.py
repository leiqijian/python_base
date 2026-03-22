#定义一个无参数有返回值的装饰器
def print_info(fn):
    def inner(): #嵌套函数，带有参数
        print("努力计算中")  # 额外功能
        return fn() #引用原函数，并把参数赋值给原函数
    return inner

#定义函数
@print_info
def func():
    a = 10
    b = 20
    return a + b

#调用函数
print(func())
