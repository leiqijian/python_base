# 编写一个函数求两个数的和
def fn1(num1, num2):
    return num1 + num2

print(fn1(10, 20))

# lambda表达式进行简化：

lambda_func = lambda num1, num2: num1 + num2
print(lambda_func(10, 20))

# 需求3: 定义一个函数, 要求传入一个字符串, 在函数内 对字符串的内容全部转换为大写( upper() ), 并且将转换后的字符串返回, 分别使用普通函数 和 lambda方式实现
# 普通函数:
# 定义函数
def fun2(s):
    return s.upper()

# 调用函数
res = fun2("qweds")
print(res)

# lambda表达式
# 定义函数
lambda_fn3 = lambda s: s.upper()

# 调用匿名函数
res = lambda_fn3("qweda")
print(res)

# 带默认参数的lambda表达式
# 函数的参数有默认值:
# 需求:  提供一个函数, 实现 2个数的求和计算操作 并且将计算结果返回  请使用 lambda方式改写
# 定义普通函数
def fn3(num1, num2=100):
    return num1 + num2

# 调用使用
res = fn3(3)
print(res)

# lambda方式
# 定义匿名函数
lambda_fn4 = lambda num1, num2=100:num1 + num2

# 使用函数
res = lambda_fn4(3)
print(res)

# 带if判断（三目运算符）的lambda表达式

# 带 if判断（三目运算符）的lambda表达式
# 有判断操作:
# 需求: 要求定义函数, 传入一个姓名, 在函数中判断, 如果姓名为张三, 返回 1 否则 返回 0
# 普通函数
def fun4(name):
    if name == "张三":
        return 1
    else:
        return 0

# 思考 函数体 能不能改成一行写出来呢?
# 格式:  条件满足返回的内容 if 条件 else 条件不满足返回的内容
def fun5(name):
    return 1 if name == "张三" else 0


# 使用函数
print(fun5("张三"))

# lambda改写: 三目运算
lambda_fn5 = lambda name: 1 if name == "张三" else 0

# 调用匿名函数
print(lambda_fn5("张三"))

# 列表数据+字典数据排序（重点）
# 案例需求: 实际场景案例
# 给定以下一个列表:
student_list = [
    {"name": "张三", "age": 20, "address": '南京'},
    {"name": "李四", "age": 25, "address": '北京'},
    {"name": "王五", "age": 23, "address": '上海'},
    {"name": "赵六", "age": 19, "address": '广州'},
    {"name": "田七", "age": 22, "address": '深圳'}
]


# 需求: 请对列表进行排序: 要求根据字典中年龄 从 大到 小 排序
# key: 是用于指定 根据 谁 进行排序 默认是列表中一个个的元素
# key 支持 接收一个函数, 函数的参数为列表的元素 根据函数的返回值 进行排序
def fun5(student_dict):
    return student_dict['age']

student_list.sort(key=fun5,reverse=True)
# lambdal
student_list.sort(key=lambda student_dict: student_dict['age'], reverse=True)

print(student_list)