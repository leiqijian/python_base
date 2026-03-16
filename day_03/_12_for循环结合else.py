# for 临时变量 in 序列:
#     循环体
# else:
#     当for循环正常结束后，返回的代码

# str1 = 'itheima'
# for i in str1:
#     if i == 'e':
#         print('遇e不打印')
#         break
#     print(i)
# else:
#     print('循环正常结束之后执行的代码')

# str1 = 'itheima'
# for i in str1:
#     if i == 'e':
#         print('遇e不打印')
#         continue
#     print(i)
# else:
#     print('循环正常结束之后执行的代码')


# 演示: for循环结合else情况
"""
    语法:
        for 临时变量 in  序列:
            循环体
        else:
            当循环正常结束后, 需要执行的代码

    如果for循环中,
        通过break退出的循环, 那么就不会执行else语句的内容
        通过continue跳过当前循环, 对于else 不会有影响的
        在循环过程中程序出现异常(程序异常结束), else也不会执行
"""
# 需求: 循环输出从 1~10, 当循环正常结束后, 打印 循环完成
for i in range(1,11):
    # 当循环到5的时候, 强制退出循环
    # if i == 5:
    #     break

    # 当循环到5的时候, 跳过当前循环 进入下一次循环
    # if i == 5:
    #     continue
    # 异常情况
    #1/0
    print(i)
else:
    print("循环结束了.....")