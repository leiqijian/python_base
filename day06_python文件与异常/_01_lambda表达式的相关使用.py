# 变量 = lambda 函数参数:表达式（函数代码 + return返回值）
# 调用变量
# 变量()

# 定义一个函数，经过一系列操作，最终返回100
def fn1():
    return 100

# 调用fn1函数
print(fn1)  # 返回fn1函数在内存中的地址
print(fn1())  # 代表找到fn1函数的地址并立即执行

# lambda表达式进行简化：
# 定义一个lambda函数
lambda_fn1 = lambda: 100
print(type(lambda_fn1))
# 使用函数
res = lambda_fn1()
print(res)