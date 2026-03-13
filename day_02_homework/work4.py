## 题目4：学生平均分计算

# 编写一个程序，让用户输入三门课程的成绩（语文、数学、英语），然后计算并输出平均分。
# 要求：
#
# 1. 使用input()分别获取三门课程的成绩
# 2. 将输入的成绩转换为浮点数
# 3. 计算平均分（保留2位小数）
# 4. 使用格式化输出，显示格式：
# 语文成绩：[成绩1]
# 数学成绩：[成绩2]
# 英语成绩：[成绩3]
# 三门课程的平均分为：[平均分]

language = round(float(input("语文成绩： ")) ,2)
math = round( float( input("数学成绩： ")), 2)
english = round(float(input("英语成绩： ")), 2)

ave = round(((language + math + english)/3), 2)
print(f"语文成绩：{language}")
print(f"数学成绩：{math}")
print(f"英语成绩：{english}")
print(f"三门课程的平均分为：{ave}")


