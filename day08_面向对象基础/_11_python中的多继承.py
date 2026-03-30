'''
多继承：同一时刻，可以同时继承多个父类
类名.父类方法名(self) 适合用于多继承子类使用父类方法
'''

class  Master():
    def __init__(self):
        print("master")
        print(self)
        skill = "[old cooking]"
        self.skill = skill

    def make_cake(self):
        print(f"I {self.skill} cook a old cake")

class School():
    def __init__(self):
        print("school")
        print(self)
        skill = "[new cooking]"
        self.skill = skill

    def make_cake(self):
        print(f"I {self.skill} cook a new cake")

class Prentice(School, Master):
    def __init__(self):
        print("Prentice")
        print(self)
        skill = "[self cooking]"
        self.skill = skill

    def make_cake(self):
        self.__init__()
        print(f"I {self.skill} cook a self cake")

    def make_school_cake(self):
        School.__init__(self) #把当前对象传到父类的init方法，使用父类的属性，再调用父类的方法
        School.make_cake(self) #如果不先init，调用父类方法的时候会使用了自己的属性

    def make_master_cake(self):
        Master.__init__(self) #把当前对象传到父类的init方法，使用父类的属性，再调用父类的方法
        Master.make_cake(self)

p1 = Prentice()
print(p1)
p1.make_cake()
print(p1)
p1.make_school_cake()
print(p1)
p1.make_master_cake()
print(p1)
p1.make_cake()
print(p1)
