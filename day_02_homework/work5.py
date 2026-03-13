# ## 题目5：长方形面积计算器
#
# 编写一个程序，让用户输入长方形的长和宽，然后计算并输出长方形的周长和面积。
#
# 要求：
#
# 1. 获取用户输入的长和宽
# 2. 将输入转换为适当的数值类型
# 3. 计算周长（周长 = 2 × (长 + 宽)）和面积（面积 = 长 × 宽）
# 4. 使用格式化输出，显示格式：
# 长方形的长为：[长]
# 长方形的宽为：[宽]
# 长方形的周长为：[周长]
# 长方形的面积为：[面积]

Length = float(input("长： "))
Wide = float(input("宽： "))

if Wide > Length:
    temp = Wide
    Wide = Length
    Length = temp

Circumference = 2 * (Length + Wide)
Area = Length * Wide

print(f"长方形的长为：{Length}")
print(f"长方形的宽为：{Wide}")
print(f"长方形的周长为：{Circumference}")
print(f"长方形的面积为：{Area}")
