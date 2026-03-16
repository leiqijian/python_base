# 演示 字符串内置的功能函数
"""
    字符串是不可变类型
    查找方法: 查找指定的字符或子串在原字符串的所在索引位置
        find() : 查不到返回 -1
        index(): 查不到会直接报错

    修改方法:
        replace() : 替换字符串
        split() : 对字符串进行切割
        title() : 将字符串每个单词首字母变为大写
        join() : 拼接字符串
"""
# 第一步: 定义一个字符串
str1 = 'apple, banana, orange'

# 第二步: 演示相关方法(API)
# 2.1 演示查找方法
# 查找 n 字符在哪个位置
# 从左往右 查找该字符在字符串出现的第一个所在位置
find = str1.find('n')
print(find)

# 从右往左 查找该字符在字符串出现的第一个所在位置
find = str1.rfind('n')
print(find)

# 查找 banana 在什么位置呢?  子串
find = str1.find('banana')
print(find)

# 演示 如果找不到  此时 返回 -1
find = str1.find('qwe')
print(find)

# 演示 index
# 当能查询到的时候, index 和 find 是一致的
index = str1.index('banana')
print(index)

# 当如果查询不到的时候: 直接报错
# index = str1.index('qwe')
# print(index)

# 演示 其他修改的方法
# 替换字符串: 将旧的字符串 替换为 新的串 返回一个新的字符串  不会修改旧的字符串
str2 = str1.replace('banana', 'pear')
print(str2)  # 输出:  apple, pear, orange
print(str1)  # 输出:  apple, banana, orange

# 切割操作: 返回一个列表,存储了切割后的多个值
# 需求: 根据  逗号 将每一个水果单词切割开
list = str1.split(',')
print(list[0])
print(list[1])
print(list[2])

# 转换为大写: 将每一个单词的首字母大写
str2 = str1.title()
print(str2) # 输出: Apple, Banana, Orange

# 字符串拼接:
# 在 传入的序列中 每一个元素的中间 拼接 字符串
# print(list) :  序列: ['apple',' banana',' orange']
str2 = str1.join(list) #字符串  'apple, banana, orange'
print(str2)  # 输出 appleapple, banana, orange bananaapple, banana, orange orange
