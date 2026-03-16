# 可以比较多个条件
# and or not
# and ：逻辑与，只有当两边的表达式全部为真，则最终结果返回为真，否则返回为假。
# or ：逻辑或，只要有一方为真，则整个表达式的返回结果就为真。除非两边的表达式都为假，则整个结果返回为假。
# not就是取反，只有一个表达式`not 表达式`，如果表达式为True，则not以后就返回False。反之，则返回True。
# 演示: 逻辑运算符
# 符号:  and  or  not
"""
    注意: 最终返回值 依然是 布尔类型

    and:
        格式:  条件1 and 条件2 and 条件3 ...
        表示: 当所有的条件都成立的时候, 返回返回True 否则都返回False

    or:
        格式:  条件1 or 条件2 or 条件3 ...
        表示: 只有当所有的条件都不成立的时候, 返回False 否则都返回True

    not:
        格式: not (and 或者 or 或者 其他条件)

        表示: 对后面的结果内容进行取反, 如果后面的结果为False  经过 not处理, 变为 True

"""
# 演示操作:
a = 10
b = 15
c = 13
d = 18

print(a < b and a < c)  # 只有都成立 返回True
print(a < b and a > c)  # 只要有条件不满足, 即返回False

print(a < b or a > c)  # 只要有条件成立 即返回True
print(a > b or a > c)  # 只有当都不成立, 返回False
print("-" * 50)

print(not (a < b or a > c))
print(not (a > b or a > c))

# 更多条件: 根据实际情况,哪些需要先对比 可以使用 () 调整优先级
print(a < b and (c < d or b < c))

'''
需求:

1- 通过键盘录入 3个int类型的数据

2- 要求各个数据 相互之间进行比较:  分别测试  > < >= <= == 结果

3- 要求将多个条件直接进行比对:   
'''


