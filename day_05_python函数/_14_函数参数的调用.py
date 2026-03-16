# 理论上，在函数定义时，我们可以为其定义多个参数。但是在函数调用时，我们也应该传递多个参数，正常情况，其要一一对应。
def user_info(name, age, address):
    print(f'我的名字{name}，今年{age}岁了，家里住在{address}')


# 调用函数
user_info('Tom', 23, '美国纽约')

# 函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
def user_info(name, age, address):
    print(f'我的名字{name}，今年{age}岁了，家里住在{address}')

# 调用函数（使用关键词参数）
user_info(name='Tom', age=23, address='美国纽约')
user_info( address='美国纽约', name='Tom', age=23)


# 缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）。
# 我们在定义缺省参数时，一定要把其写在参数列表的最后侧
def user_info(name, age, gender='男'):
    print(f'我的名字{name}，今年{age}岁了，我的性别为{gender}')


user_info('李林', 25)
user_info('振华', 28)
user_info('婉儿', 18, '女')
