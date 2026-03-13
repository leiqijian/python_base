# ## 题目3：旅行时间计算器
#
# 编写一个程序，让用户输入出发时间和到达时间（24小时制的小时数，如8表示8:00），然后计算并输出旅行所用小时数：
# 出发时间：[出发时间]:00
# 到达时间：[到达时间]:00
# 旅行用时：[用时]小时
# 要求：
#
# 1. 获取出发时间和到达时间的输入
# 2. 将输入转换为整数
# 3. 计算用时（到达时间-出发时间）
# 4. 使用格式化输出显示结果
# 获取用户输入
departure = input("请输入出发时间（24小时制的小时数，如8表示8:00）：")
arrival = input("请输入到达时间（24小时制的小时数，如8表示8:00）：")

# 将输入转换为整数
departure_hour = int(departure)
arrival_hour = int(arrival)

# 计算用时
if arrival_hour >= departure_hour:
    travel_time = arrival_hour - departure_hour
else:
    travel_time = (24 - departure_hour) + arrival_hour

# 格式化输出
print(f"出发时间：{departure_hour}:00")
print(f"到达时间：{arrival_hour}:00")
print(f"旅行用时：{travel_time}小时")