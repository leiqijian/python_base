import copy

tuple1 = (1,2,3, [4,5])

tuple2 = copy.copy(tuple1)
print(id(tuple1)) #1698365083776
print(id(tuple2)) #1698365083776

print(id(tuple1[3])) #1698364865408
print(id(tuple2[3])) #1698364865408
