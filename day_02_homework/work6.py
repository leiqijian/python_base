## 题目6：购物清单计算器

# 编写一个程序，让用户输入商品名称、单价和购买数量，然后计算总金额并输出以下格式：
# 您购买了[商品名称]，单价[单价]元，数量[数量]件，总金额为[总金额]元。
# 要求：
#
# 1. 使用input()函数分别获取三个输入
# 2. 将单价和数量转换为适当的数值类型
# 3. 计算总金额（单价×数量）
# 4. 使用f-string格式化输出，总金额保留2位小数

name = str(input("product name:"))
price = float(input("product price:"))
count = int(input("count of product:"))

total_price = price * count

print(f"您购买了{name}，单价{price}元，数量{count}件，总金额为{total_price}元。")


