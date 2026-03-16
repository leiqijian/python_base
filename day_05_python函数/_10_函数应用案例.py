"""
需求: 奇偶求和.
    编写一个程序，求出一个列表中偶数和奇数的和。

    定义函数calculate_sum()，参数为一个数字列表numbers_list, 分别求出偶数和奇数的和。
    最后，返回一个列表(元组)，第一个元素为偶数的和，第二个元素为奇数的和。
"""


# 定义功能函数:  接收一个 数字列表 然后 求这个列表中 奇数和   和  偶数和 并且 将这二个结果返回
def calculate_sum(numbers_list):
    j_sum = 0
    o_sum = 0
    for number in numbers_list:
        # 奇数和
        if number % 2 == 1:
            # 奇数
            j_sum += number
        else:
            # 偶数和
            o_sum += number

    # 到这里后, 奇数和  和  偶数和 全部计算完成
    # 将结果返回
    return o_sum, j_sum


# 使用函数
number_list = [3, 5, 7, 2, 1, 8, 9, 10]

res = calculate_sum(number_list)

print(res)
print(type(res))