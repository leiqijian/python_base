# class Person(object):
#     age = None
#     name = None
#
#     def __init__(self, name):
#         self.name = name
#         self.age = 18
#
#     def __str__(self):
#         return f"Student('{self.name}', {self.age})"
#
# p1 = Person("tom")
# print(p1)
# print(p1.name)
# print(p1.age)

class Person():
    # 封装属性
    age = None
    name = None
    # 封装方法
    def eat(self):
        print(f"{self.name}今年{self.age}岁了，在吃午饭")

P1 = Person()
P1.age =18
P1.name = "tom"
P1.eat()


