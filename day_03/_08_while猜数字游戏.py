# 编写一个Python程序，随机生成一个1到100之间的整数，用户通过输入猜测的数字，
# 程序会根据用户的输入提示“猜大了”、“猜小了”或“猜对了”。
# 用户可以无限次猜测，直到猜对为止。猜对后，程序会提示用户并结束游戏。
import random

computer_number = random.randint(1,100)
print(computer_number)
i = 1
while i <= 5:
    a = int(input("请输入一个1～100的随机数"))
    if computer_number == a:
        print("猜对了")
        break
    else:
        if computer_number > a:
            print("")
        if computer_number < a:
            print("")
        i = i + 1