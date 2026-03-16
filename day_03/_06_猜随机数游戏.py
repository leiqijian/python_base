import random
# 猜数字小游戏
# 1- 随机生成一个随机数
random_num = random.randint(1, 100)
print(random_num)
# 2- 让用户输入一个1~100的数字
user_num = int(input("欢迎来到猜数字小游戏, 你只有一次机会哈, 请输入一个整数(1~100):"))

# 3- 比较: 猜对了 猜大了 猜小了  (if嵌套玩法)
# if user_num == random_num:
#     print("恭喜你, 猜对了....")
# else:
#     # 如果能执行else里面的内容, 说明一定没猜对, 有可能是猜大了 也有可能猜小了
#     if user_num > random_num:
#         print("你猜大了...")
#     else:
#         print("你猜小了....")

if user_num == random_num:
    print("恭喜你, 猜对了....")
elif user_num > random_num:
    print("你猜大了...")
else:
    print("你猜小了....")

