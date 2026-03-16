# 演示 自动拆包
# 注意: 容器中有几个值, 需要 有几个变量接受这个值
# 1- 定义一个容器
tuple1 = ("张三", True, 18)  # 最常用
# tuple1 = ["张三", True, 18]
# tuple1 = {"张三", True, 18}  虽然支持 单一般不用

# 2- 需求: 将元组中每一个元素 分别赋值给 name  is_flag  age 三个变量
# name = tuple1[0]
# is_flag = tuple1[1]
# age = tuple1[2]
name, is_flag, age = tuple1  # 自动拆包

print(f"{name},{is_flag},{age}")
 
# 3- 其他自动拆包
a, b = (10, 20)
print(f"{a},{b}")
a, b = 10, 20
print(f"{a},{b}")

# 案例需求:
# 实现两个变量值的交换：  c1 = '可乐'  c2 = '牛奶'

# 1- 初始化二个变量
c1 = '可乐'
c2 = '牛奶'

# # 2- 转换为 元组
# tuple2 = (c1, c2)
#
# # 3- 执行交换操作
# c2,c1 = tuple2  # 等价于 c2, c1 = ('可乐', '牛奶')
#
# print(c1)
# print(c2)

# 2- 直接交换
# c2, c1 = c1, c2
#
# print(c1)
# print(c2)


# 方式三: 不使用 自动拆包:
# 借用 第三个临时变量
c1 = '可乐'
c2 = '牛奶'

# 临时变量
tmp = c1

# 交换
c1 = c2
c2 = tmp

print(c1)
print(c2)