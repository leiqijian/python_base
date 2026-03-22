def loggin(flag):
    def decorator(fn):
        def inner(sum1, sum2):
            if flag == "+":
                print("正在做加法运算")
            elif flag == "-":
                print("正在做减法运算")
            result = fn(sum1, sum2)
            return result

        return inner
    return decorator

@loggin("+")
def add(a, b):
    return a + b

@loggin("-")
def subtract(a, b):
    return a - b

result = add(1, 2)
result = subtract(1, 2)

#分析
# 1. 定义 loggin 函数（外层函数）
def loggin(flag):
    def decorator(fn):
        def inner(sum1, sum2):
            if flag == "+":
                print("正在做加法运算")
            elif flag == "-":
                print("正在做减法运算")
            result = fn(sum1, sum2)
            return result
        return inner
    return decorator

# 2. 遇到 @loggin("+") - 装饰器语法糖展开
@loggin("+")
def add(a, b):
    return a + b

# 等价于以下执行顺序：
# step1: 调用 loggin("+") -> 返回 decorator 函数
# step2: 将 decorator 函数应用到 add 函数上
# step3: add = decorator(add)

# 详细执行：
temp_decorator = loggin("+")  # ① 执行 loggin 函数
# 在 loggin 内部：
#   - flag = "+"
#   - 定义 decorator 函数
#   - 返回 decorator

add = temp_decorator(add)  # ② 调用 decorator(add)
# 在 decorator 内部：
#   - fn = add（原始的 add 函数）
#   - 定义 inner 函数（闭包，记住了 flag="+" 和 fn=原add）
#   - 返回 inner

# 最终：add 变量现在指向 inner 函数

# # 语法糖写法
# @loggin("+")
# def add(a, b):
#     return a + b
#
# # 等价于
# def add(a, b):
#     return a + b
# add = loggin("+")(add)
#
# # 也可以写成
# add = loggin("+")(lambda a, b: a + b)
