# 演示 文件的读写操作
# 演示 写入数据到文件
# 1- 打开文件
# 路径地址:
"""
    绝对路径
        直接从盘符往下 整个路径 就是绝对路径  不关心你当前在哪个路径
    相对路径
        相对你当前的这个文件, 你要查询的文件在哪里
        ./ 当前路径  可以省略, 当从当前路径 往下的查询的时候
        ../ 上一级路径
        ../../  上上级路径


"""
#f = open(file="C:/soft/PyCharm_2023.2.5/workspace/day06_python/data/a.txt",mode='w')
f = open(file="./data/a.txt",mode='w')
# 2- 执行相关操作
f.write("hijklmn")
# 3- 关闭文件
f.close()

# 1、打开文件
f = open('./data/python.txt', 'w', encoding='utf-8')
# 2、写入内容
f.write('人生苦短，我学Python！')
# 3、关闭文件
f.close()
