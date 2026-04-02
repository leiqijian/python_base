import copy

list1 = [1, 2, 3, [4, 5, 6]]

list2 = copy.copy(list1)

print(list1) #[1, 2, 3, [4, 5, 6]]
print(list2) #[1, 2, 3, [4, 5, 6]]
list2[0] = 5
print(list2) #[5, 2, 3, [4, 5, 6]]
list2[3][0] = 7
print(list1) #[1, 2, 3, [7, 5, 6]]
print(list2) #[5, 2, 3, [7, 5, 6]]

print(id(list1)) #1701886076800
print(id(list2)) #1701887033152