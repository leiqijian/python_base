# 使用元组，元组可以存储多个数据且元组内的数据是不能修改的。
# 列表可以一次性存储多个数据，但是列表中的数据允许更改。
# 1- 如何定义元组
# 格式:
#   变量名称 = (元素1,元素2,元素3......)
#   变量名称 = (元素1,) : 如果元组中只有一个元素, 必须在后面添加一个逗号 否则编译器会自动转换为 数据的本身类型, 而不是元组类型
userTuple = ('张三','李四','王五',10,20,30,True,False)
print(userTuple)
print(type(userTuple))

tuple1 = ('张三',)
print(tuple1)
print(type(tuple1))

# 2- 如何使用元组
# 2.1 获取元组中某个元素:  与 列表 和 字符串 一致 都是通过索引的方式来获取
print(userTuple[0])
print(userTuple[1])
print(userTuple[2])

# 2.2 遍历: 与 列表 一致

# 2.3 获取某个元素在元组中索引值: index
print(userTuple.index(True))

# 2.4 获取某个元素在元组中出现了几次
print(userTuple.count('王五'))

# 2.5 获取元组长度
print(len(userTuple))
