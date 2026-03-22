# 定义一个函数
# describe_inputs，该函数使用 * args
# 接收任意数量的位置参数，使用 ** kwargs
# 接收任意数量的关键字参数。 函数的功能是： 打印出通过 * args接收到的参数个数。 打印出通过 ** kwargs接收到的参数个数。
# 打印出 ** kwargs中所有的键（key）。 示例调用： describe_inputs(1, 'hello', 3.14, name='Alice', age=25, city='Beijing')
# 示例输出： 位置参数个数: 3
# 关键字参数个数: 3
# 关键字参数的键: name, age, city

def describe_inputs(*args, **kwargs):
    print(f"位置参数个数:{len(args)}")
    print(f"关键字参数个数:{len(kwargs)}")
    result = []
    for key in kwargs.keys():
        result.append(key)
    print(f"关键字参数的键{result}")


describe_inputs(1, 'hello', 3.14, name='Alice', age=25, city='Beijing')


