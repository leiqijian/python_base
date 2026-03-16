userList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

for e in userList:
    print(e)

# 演示: 如何定义列表
# 格式: 变量名称 = [元素1,元素2,元素3......]
# 需求: 构建一个列表, 保存 张三 李四 王五 赵六 四个名字
userList = ['张三','李四','王五','赵六']
print(userList)

# 如何获取列表中某一个元素呢? 与 字符串 一致
print(userList[0])
print(userList[1])
print(userList[2])

# 如何遍历列表呢?
print("-----------------")
# for循环
for e in userList:
    print(e)

# while循环
print("-----------------")
# 计数器
i = 0

while i < len(userList):
    print(userList[i])

    # 更新计数器
    i += 1