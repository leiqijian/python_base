"""
    read(size):  读取文件中内容(采用二进制方式 支持读取 文本\图片\视频\音频等格式)
        参数: size  指调用一次read函数 从文件中读取多少个字符或字节  如果不传递将文件全部读取

    readlines():
        读取文件中内容(通过一行一行方式来读取, 一次性将所有行全部都读取, 保存到一个列表中) 仅能读取文本
        如果想拿到每一行的数据, 需要遍历返回来的列表

    readline():
        读取文件中内容(一次只读取一行数据) 仅能读取文本, 当读取不到的时候, 返回 空
        想基于此API读取文件中所有行, 就要使用 循环方式 一次一次读取即可

"""
# 1- 打开文件
f = open(file='data/b.txt', mode='r', encoding='UTF-8')
# 2- 执行相关操作: 读取文件
# read函数
# content = f.read(10)
# print(content)

# readlines 函数
# line_list = f.readlines()
# # 获取每一行数据
# for line in line_list:
#     print(line)

# readline 函数
while True:
    line = f.readline()
    # 当读取不到的时候, 说明已经读完了, 直接退出循环
    if not line:
        break

    print(line)

# 3- 关闭文件
f.close()
