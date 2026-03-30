'''
类属性：不是某个对象所拥有，是整个类以及所有对象公用的属性
类属性作用：追踪实例对象的数量，保存与类相关的配置等
语法：类.属性名
'''

class Student(object):
    #定义一个类属性， 给类加的属性，属于整个类，所有对象共享
    count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1

s1 = Student("leimen", 100)
print(s1.count) #通过对象.属性名获取类属性
s2 = Student("Jenny", 90)
print(s2.count)  #通过对象.属性名获取类属性
print(Student.count)  #通过类.属性名获取类属性 ，推荐做法

print("""----------------""")
s1.count = 99
print(s1.count) #99 相当于给s1对象创建了一个count属性，是对象属性，与类属性脱钩了
print(s2.count) #2
print(Student.count) #2


