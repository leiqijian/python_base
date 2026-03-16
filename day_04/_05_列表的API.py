# 演示列表的API
userList = ['张三', '李四', '王五', '赵六', '田七', '周八', '李九', '李四']
# 查询相关方法:
# 1- index(): 查询指定数据所在位置的下标  如果不存在 直接报错
index = userList.index("赵六")
print(index)  # 3

# 2- count(): 统计数据在当前列表中出现的次数
count = userList.count("李四")
print(count)  # 2

# 3- in 和 not in 判断是否存在或不存在
bool = "王五" in userList
print(bool)
bool = "王五" not in userList
print(bool)

# 增加函数
# 1- append()  增加指定数据到列表中
# 如果 老王 不在列表中, 请增加到列表中
if "老王" not in userList:
    # 能进来, 说明 老王 不在, 如果不在 添加到列表中
    userList.append("老王")

print(userList)

# 2- extend(): 将一个序列 追加到另一个序列中
# 2.1 先定义一个新的序列
user2List = ['老李', '老刘']

# 2.2 将新列表中数据 增加 到 原有列表中
userList.extend(user2List)

print(userList)

# 3- insert() 在指定位置新增数据
userList.insert(4, '小田')

print(userList)

# 删除操作
# 1- del 列表[索引]
del userList[-1]

print(userList)

# 2- pop() 删除指定下标的数据, 默认是删除最后一个 并且会返回删除的数据
element = userList.pop()
print(element)
print(userList)

element = userList.pop(2)
print(element)
print(userList)

# 3- remove() 移除列表中某个指定数据  如果不存在, 也不会报错 无效果
userList.remove("小田")
print(userList)

# 修改操作
# 1-  修改某个索引的值
userList[0] = '老张'
print(userList)

# 2- reverse: 反转操作
userList.reverse()

print(userList)

# 3- 排序操作: reverse 设置 是否反转   True 反转(倒序)  False 不反转(正序)
list1 = [2, 5, 9, 67, 1, 8, 3, 4]
list1.sort(reverse=True)
print(list1)