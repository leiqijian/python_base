# 推导式演示:
"""
    格式:
        变量名 = [表达式 for 变量 in 列表]
        变量名 = [表达式 for 变量 in 列表 if 条件]
        变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]

"""

# 案例1：定义0-9之间的列表
# 非推导式方式
my_list = []

for i in range(0, 10):
    my_list.append(i)

print(my_list)

# 推导式:
my_list = [i for i in range(0, 10)]
print(my_list)

# 案例2: 给定一个列表, 将该列表内容依次添加到另一个集合中, 实现去重效果 得到一个集合:  {7,9,5,4,6}
my_list2 = [7, 9, 5, 4, 5, 7, 6]

# 非推导方式:
my_set1 = set()

for e in my_list2:
    my_set1.add(e)

print(my_set1)

# 推导式方式:
my_set2 = {e for e in my_list2}
print(my_set2)

# 列表推导式 + if条件判断
# 变量 = [表达式 for 临时变量 in 序列 if 条件判断]
#
# 等价于
#
# for 临时变量 in 序列:
#     if 条件判断

#  推导式 含  IF 操作
# 格式: 变量 = [表达式 for 临时变量 in 序列 if 条件判断]

# 需求: 案例：生成0-9之间的偶数（i%2  0）序列
# 非推导式方式
my_list3 = []
for e in range(0, 10):
    if e % 2 == 0:
        my_list3.append(e)


print(my_list3)

# 推导式:
my_list4 = [e for e in range(0, 10) if e % 2 == 0]

print(my_list4)

# 需求2: 生成 0~9的序列, 然后将 > 5的数据 存储到一个新的列表中
# 推导式
my_list5 = [ e for e in range(0,10) if e > 5 ]
print(my_list5)

# for循环嵌套列表推导式
# for 临时变量 in range(n):
#     for 临时变量 in range(n):
# 变量 = [表达式 for 临时变量 in 序列 for 临时变量 in 序列]

# 创建列表 => [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 原生代码：for循环嵌套
list1 = []
# 外层循环
for i in range(1, 3):
    # 内层循环
    for j in range(0, 3):
        tuple1 = (i, j)
        list1.append(tuple1)
print(list1)

# 演示 推导式中 for循环嵌套:

# 需求:  生成这个序列: [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 非推导式研究
my_list6 = []

for i in range(1,3):
    for e in range(0,3):
        my_list6.append((i,e))

print(my_list6)

# 推导式方式
my_list7 = [(i,e) for i in range(1,3)  for e in range(0,3) ]

print(my_list7)