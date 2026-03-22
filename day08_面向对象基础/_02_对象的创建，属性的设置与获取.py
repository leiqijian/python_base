# 定义一个对象

class Person():
    pass

# 实例化对象

p1 = Person()

# 对象赋值
p1.age = 18
p1.name = 'tom'

# 属性获取
print(p1) #打印的是p1在内存中的地址,可通过魔术方法得到这个对象的属性
print(p1.name)
print(p1.age)