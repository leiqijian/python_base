'''
使用类似推到式的语法，创建一个生成器，比如的到0，2，4，6，8
'''

#传统做法
list1 = []
for i in range(0, 5):
    print(i)
    list1.append(i * 2)

print(list1)

gen2 = (i * 2 for i in range(0, 5))
print(gen2)
#<generator object <genexpr> at 0x00000295EBED8EE0>
# 几乎不占用内存，只是提前生成了一个用于生成0，2，4，6，8的规则，后期按需生成

# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))

for i in gen2:
    print(i)
