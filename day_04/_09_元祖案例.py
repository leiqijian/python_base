# 编写一个程序来提取嵌套元组中的唯一元素。
# 例如: 在嵌套元组((1,2,3),(2,4,6),(2,3,5))中, 2重复出现了3次，3重复出现了2次，但我们的输出列表只会包含2、3一次。
# 即：[1, 2, 3, 4, 5, 6]

tuple1 = ((1,2,3),(2,4,6),(2,3,5))

result = []

for e in tuple1:
    for i in e:
        if i not in result:
            result.append(i)

print(result)


# 给定一个元组my_tuple，里面包含1, 2, 3, 4, 5, 6, 7, 8, 9元素，要求统计数字元组中, 奇数的个数
my_tuple = (1,2,3,4,5,6,7,8,9)
result = []

for e in my_tuple:
    if e % 2 == 1:
        result.append(e)
        print(e)
print("---------")
print(len(result))
