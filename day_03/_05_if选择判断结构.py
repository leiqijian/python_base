'''
if 条件判断:
    则执行某段代码...

print()
'''

# 需求: 让用户输入一个年龄, 判断其年龄是否大于等于 18岁 如果大于等于了, 打印 你已经成年了, 可以去网吧了

# age = int(input("请输入年龄"))
# if age >= 18:
#     print("你已经成年了, 可以去网吧了")
# else: print("未成年")

# 比如 成绩判断  当成绩  >= 90  优秀   >=80 良好  >= 70 中等  >=60 及格  否则 不及格
# score =  round(float(input("请输入成绩")),2)
#
# print(score)
#
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 70:
#     print("中等")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")
#

# 案例：法律规定，车辆驾驶员的血液酒精含量小于 20mg/100ml 不构成酒驾；
# 酒精含量大于或等于 20mg/100ml 为酒驾；
# 酒精含量大于或等于 80mg/100ml 为醉驾。
# 编写 Python 程序判断是否为酒后驾车。
#
# value = float(input("输入酒精含量"))
#
# print(value)
#
# if value >= 20:
#     if value > 80:
#         print("醉驾")
#     if value >= 20:
#         print("酒驾")
# else:print("正常")


# 判断
mg = int(input("请输入每100ml的酒驾含量:"))
if mg < 20:
    print("你不构成酒驾,不扣分 不罚钱")
else:
    if mg >= 80:
        print("哥们, 你已经是醉驾状态, 扣12分 罚款 200 拘留15日")
    else:
        print("你酒驾了...")