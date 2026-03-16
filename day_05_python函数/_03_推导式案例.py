# 推导式案例: 案例一：使用列表推导式生成平方数集合
# 例如, 用户输入10, 表示要生成 1~10的每一个数字的2平方的集合
# 1- 让用户输入一个正整数
n = int(input("请输入一个正整数:"))

# 2- 遍历 从 1 ~ N
# 2.1 初始化一个空列表
my_list7 = []
for j in range(1,n+1):
    # 2.2 计算 2的平方 将结果写入列表
    my_list7.append(j ** 2)

print(my_list7)

# 推导式 如何解决
my_list8 = [ j ** 2 for j in range(1,n+1)]
print(my_list8)