#定义一个有参数无返回值的装饰器
def print_info(fn):
    def inner(x ,y): #嵌套函数，带有参数
        print("努力计算中")  # 额外功能
        fn(x, y) #引用原函数，并把参数赋值给原函数
    return inner

#定义函数
@print_info
def func(x ,y):
    z = x + y
    print(f"a + b = {z}")

#调用函数
func(10, 20)
