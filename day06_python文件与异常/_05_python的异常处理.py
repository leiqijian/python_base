# 演示 猜数字小游戏
# 1- 随机生成一个1~100的整数
import random

computer_number = random.randint(1,100)
print(computer_number)
# 2- 让用户猜: 写死循环方式

# 定义 总计猜测次数
count = 1

print("欢迎你来到猜数字小游戏的环节....")
while True:
    # 2.1 让用户输入一个1~100整数
    user_number = int(input("请输入一个1~100的整数:"))
    # 2.2 通过 if 判断 用户输入的内容 是否正确 (猜对了 猜大了 猜小了)
    if user_number == computer_number:
        print(f"恭喜你, 猜对了, 您在第{count}次就猜对了, 游戏结束...")
        # 注意: 当用户猜对了, 需要退出循环
        break
    else:
        if 5-count <= 0:
            print("不好意思, 次数已经用完了, 您没有猜出来.......")
            break

        if user_number > computer_number:
            print(f"不好意思, 你猜大了, 请重新猜,您还剩余{5-count}次机会......")
        else:
            print(f"不好意思, 你猜小了, 请重新猜,您还剩余{5-count}次机会......")

        # 计数器 + 1
        count += 1

    if count > 5:
        break
