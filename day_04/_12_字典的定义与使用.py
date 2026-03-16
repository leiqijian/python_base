# 1- 演示: 如何定义字典
# 格式:
#   格式1:  变量名称 = {key1:value1,key2:value2,key3:value3.....}
#   格式2:  变量名称 = {}  或者 变量名称 = dict()   空字典

# 构建一个有内容的字典
person = {'name': '张三', 'age': 18, 'address': "南京市雨花台区板桥镇", 'sex': '男', 'hobby': '羽毛球、乒乓球、台球'}
print(person)
print(type(person))

# 构建空字典
dict1 = {}
dict2 = dict()
print(dict1)
print(type(dict1))
print(dict2)
print(type(dict2))

print("---------分割符---------")

# 遍历操作
for key in person:
    print(f"key:{key}")
    print(f"value:{person[key]}")
    print("------")

# API
# 字典的相关API:
# 如何增加元素:
# 需求: 为person 字典增加一个 birthday 属性 值为 2007-10-15
person["birthday"] = '2007-10-15'  # 字典[key] = 'value'

print(person)

# 如何修改元素: 与添加一直, 如果key存在就是修改 如果不存在 就是添加
# 需求: 修改性别为 女
person['sex'] = "女"
print(person)

# 如何删除元素
# 删除某个元素:  根据key
del person['birthday']
print(person)
# 清空字典
# person.clear()
# print(person)

# 如何查询:
# 1- 根据 key 直接获取value: 如果key 不存在 直接报错
# 获取 address的值
print(person['address'])

# 2- 获取所有的keys
keys_list = person.keys()
print(keys_list)
# 3- 获取所有的value
values_list = person.values()
print(values_list)
# 4- 获取字典中每一个 kv对
# 快速返回变量: ctrl + alt + v

print("---------分割符2---------")
items = person.items()
print(items)

for kv in items:
    print(kv)
    print(f'{kv[0]},{kv[1]}')
