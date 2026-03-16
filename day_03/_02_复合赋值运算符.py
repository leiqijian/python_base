# 复合赋值运算符的计算顺序 = 先执行算术运算符，执行完毕后，把结果在赋值给左边的变量。
# 当2个变量进行算术运算时，需要将运算结果赋值给左边的变量的时候

a = 10
b = 5

a = a * b

a *= b

print(a)


# 需求: 假设你是一位很棒的AA制餐厅的服务员，你的任务是计算每位顾客的应付金额。
# 输入顾客人数，并赋值给total_friends变量。
# 输入总账单数值，并赋值配给 total_bill 变量。
# 在账单费用上加上20%的税，并计算最终账单总额均摊给顾客金额，然后打印

total_friends = int(input("顾客人数"))
total_bill = float(input("总账单金额"))

total_bill *= 1.2

avg_bill = total_bill / total_friends

print(f"每位顾客需要均摊{avg_bill}")