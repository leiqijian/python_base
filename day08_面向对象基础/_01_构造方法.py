# # 方式1：在 __init__ 中定义属性（推荐）
# class Person1:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def speak(self):
#         print(f'名字：{self.name}，年龄：{self.age}，住址：{self.address}')
#
#
# p1 = Person1('孙悟空', 500, '花果山')
# p1.speak()  # 名字：孙悟空，年龄：500，住址：花果山

#
# # 方式2：动态添加属性（灵活但容易出错）
# class Person2:
#     def speak(self):
#         print(f'名字：{self.name}，年龄：{self.age}')
#
#
# p2 = Person2()
# p2.name = '猪八戒'
# p2.age = 300
# p2.speak()  # 名字：猪八戒，年龄：300


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # 面向用户：友好、易读
        # return f"学生：{self.name}，{self.age}岁"
        return f"Student('{self.name}', {self.age})"

    def __repr__(self):
        # 面向开发者：精确、无歧义、最好能重现对象
        return f"Student('{self.name}', {self.age})"


# 测试
s = Student('张三', 20)

print(str(s))  # 学生：张三，20岁
print(repr(s))  # Student('张三', 20)

print(s)  # 学生：张三，20岁（print调用__str__）
s  # 在交互式环境：Student('张三', 20)（显示__repr__）


