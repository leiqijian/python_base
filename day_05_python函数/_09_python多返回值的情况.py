def return_num():
    return 1, 2


result = return_num()
print(result)
print(type(result))  # <class 'tuple'>

# 需求: 请帮我定义一个函数: computer 计算器函数, 要求给这个函数传入 2个参数, 在函数的内部完成  + - 计算, 并且将 + -的二个结果返回

# 定义函数:
def computer(a, b):
    # 编写函数功能的核心位置
    jia = a + b
    jian = a - b

    # 将加和减结果一并返回
    return jia, jian
    # return [jia, jian]
    # return {jia, jian}
    # return {'jia':jia,'jian':jian}


# 调用函数
# res = computer(3,5)
i,j = computer(3,5)  # 利用自动拆包思想

print(f'加法结果:{i},减法的结果:{j}')
