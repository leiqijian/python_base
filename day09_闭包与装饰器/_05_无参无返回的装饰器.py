# 定义装饰器
def print_info(fn):
    def inner(): #嵌套函数
        print("努力计算中") #额外功能
        fn() #引用原函数
    return inner #有返回

#定义函数并使用语法糖
@print_info
def get_sum():
    a = 10
    b = 20
    c = a + b
    print(f"a + b = {c}")

#调用函数
get_sum()