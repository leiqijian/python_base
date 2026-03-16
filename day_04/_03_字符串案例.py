# 将字符串向右旋转n位，例如“abcdef”向右旋转2位得到“efabcd”
# 1- 初始化原始的字符串
str1 = 'abcdef'

# 2- 键盘录入一个N: 表示右旋几位
n = int(input("请输入要右旋N位:"))

# 3- 执行右旋操作
# 3.0 考虑: 如果用户输入的值 大于 了 字符串的长度 怎么办?
n = n % len(str1)

# 3.1 根据右旋N位, 将字符串进行切割
s1 = str1[-n:]  # ef
s2 = str1[:-n]  # abcd

# 3.2 拼接完成最终结果:  efabcd
str2 = s1 + s2

print(str2)
