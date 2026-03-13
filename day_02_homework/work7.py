# ## 题目2：简单储蓄计算器
#
# 编写一个程序，让用户输入每月储蓄金额和储蓄月数，然后计算总储蓄金额并输出：
# 每月储蓄金额：[金额]元
# 储蓄月数：[月数]个月
# 总储蓄金额：[总金额]元
# 要求：
# 1. 获取用户输入的每月储蓄金额和月数
# 2. 将输入转换为适当的数值类型
# 3. 计算总储蓄金额（每月金额×月数）
# 4. 使用格式化输出显示结果，总金额保留2位小数

amount_pre_month = round(float(input("每月储蓄金额: ")), 2)
months = int(input("储蓄月数:"))

total_amount = amount_pre_month * months

print(f"每月储蓄金额：{amount_pre_month}元")
print(f"储蓄月数：{months}个月")
print(f"总储蓄金额：{total_amount}元")