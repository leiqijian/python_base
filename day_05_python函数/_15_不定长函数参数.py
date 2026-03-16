# 不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数(不传参也可以)的场景。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。
# 不定长元组（位置）参数
def user_info(*args):
    # print(args)  # 元组类型数据，对传递参数有顺序要求
    print(f'我的名字{args[0]}，今年{args[1]}岁了，住在{args[2]}')

# 调用函数，传递参数
user_info('Tom', 23, '美国纽约')

# 不定长字典（关键字）参数
def user_info(**kwargs):
    # print(kwargs)  # 字典类型数据，对传递参数没有顺序要求，格式要求key = value值
    print(f'我的名字{kwargs["name"]}，今年{kwargs["age"]}岁了，住在{kwargs["address"]}')

# 调用函数，传递参数
user_info(name='Tom', address='美国纽约', age=23)

# 综上：无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程。
#
# Python组包：就是把多个数据组成元组或者字典的过程。

# 演示不定长参数:
# 不定长元组（位置）参数
# 定义函数:
def fun1(*args):  # 这种 一个 * 不定长参数, 背后 是一个容器(序列) --> 元组
    # 获取每一个参数的内容
    print(type(args))
    for e in args:
        print(f"参数:{e}")


# 调用函数
fun1("张三", "李四", "王五", "赵六", "田七")


# 不定长字典(关键词)参数
def fun2(**kwargs):  # 这种 一个 ** 不定长参数, 背后 是一个容器(序列) --> 字典
    print(type(kwargs))
    # 遍历参数
    for key in kwargs:
        print(f"参数的key:{key}, 对应的值为:{kwargs[key]}")

# 调用函数: 必须使用关键词传参
fun2(name="张三", age=18, address="南京市")  # 在调用的时候, 创建了一个字典, 将 kv数据放置到了字典中


def func(*args, **kwargs):
    print(args)
    print(kwargs)


# 定义一个元组（也可以是列表）
tuple1 = (10, 20, 30)
# 定义一个字典
dict1 = {'first': 40, 'second': 50, 'third': 60}
# 需求：把元组传递给*args参数，字典传递给**kwargs
# ① 如果想把元组传递给*args，必须在tuple1的前面加一个*号
# ② 如果想把字典传递给**kwargs，必须在dict1的前面加两个**号
func(*tuple1, **dict1)