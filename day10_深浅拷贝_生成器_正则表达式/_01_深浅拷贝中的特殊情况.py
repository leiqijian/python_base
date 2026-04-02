import copy

# tuple1 = (1,2,3, [4,5])
#
# tuple2 = copy.copy(tuple1)
# 对于不可变数据，没有浅拷贝，相当于两个变量同时指向了一个相同的地址
# print(id(tuple1)) #1698365083776
# print(id(tuple2)) #1698365083776
#
# print(id(tuple1[3])) #1698364865408
# print(id(tuple2[3])) #1698364865408

# tuple1 = (1,2,3, (4,5))
#
# tuple2 = copy.deepcopy(tuple1)
# print(id(tuple1)) #1746096206320
# print(id(tuple2)) #1746096206320
#
# print(id(tuple1[3])) #1706647286912
# print(id(tuple2[3])) #1706648827392

# 不可变套可变 tuple套list
tuple1 = (1,2,3, [4,5])
# tuple1 = (1,2,3, 4)

tuple2 = copy.deepcopy(tuple1)
print(id(tuple1)) #1775405609456
print(id(tuple2)) #1775405609056

#可变套不可变 list套tuple
# list1 = [1,2,3, (4,5)]
#
# list2 = copy.deepcopy(list1)
# print(id(list1)) #2514301117824
# print(id(list2)) #2514301265792
