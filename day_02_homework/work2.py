## 题目2：简易计算器

# 编写一个程序，让用户输入两个数字，然后计算并显示：
#
# 1. 两个数字的和
# 2. 两个数字的差
# 3. 两个数字的乘积
# 4. 第一个数字除以第二个数字的商（保留2位小数)

number1 = float(input("请输入第一个数字 : "))
number2 = float(input("请输入第二个数字 : "))

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(round(number1 / number2, 2))
print(float("{:.2f}".format(number1 / number2)))