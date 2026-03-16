# 1- 函数定义:
"""
    语法:
        def 函数名称([参数1,参数2,参数3....]):
            函数体(该函数实现具体的功能代码块)

            [return 返回值]

    函数:
        不调用 不执行

"""
# 通过购票方案分别演示: 不使用函数、有函数、带参数、有返回值几种玩法

# 1- 定义一个总票数:
ticket = 100


# 卖票逻辑:
# 执行卖票
# ticket -= 1
# print(f"卖出1张票, 剩余{ticket}")
#
# ticket -= 1
# print(f"卖出1张票, 剩余{ticket}")
#
# ticket -= 1
# print(f"卖出1张票, 剩余{ticket}")
#
# ticket -= 1
# print(f"卖出1张票, 剩余{ticket}")

# 利用函数思想:
# 定义一个函数, 执行卖票
def sale_ticket():
    # ticket -= 1
    # 验证用户信息
    # 获取购买哪里的票
    # 查询是否还有票
    # 触发 -1 卖票逻辑
    print("卖出1张票")


# 调用该函数: 执行卖票
sale_ticket()
sale_ticket()
sale_ticket()
sale_ticket()


# 思考: 如果希望在卖票的时候, 打印是谁买了票的信息
# 函数 带参数
def sale_ticket_1(name):
    print(f"卖出1张票,卖给了{name}")


# 调用函数
sale_ticket_1("张三")


# 函数带返回值
# 希望 在卖票完成后, 告知给调用方, 卖票成功
def sale_ticket_2(name):
    print(f"卖出1张票,卖给了{name}")

    return True

# 调用
flag = sale_ticket_2("李四")

if flag:
    print("卖票成功")
else:
    print("卖票失败")

def sum_numbers(num1, num2):
    return num1 + num2


print(sum_numbers(10, 20))