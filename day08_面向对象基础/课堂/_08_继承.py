class Person(object):
    def __init__(self, name = "zhangsan"):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
class Student(Person):
    pass
class Teacher(Person):
    pass

s1 = Student()
s1.eat()
s2 = Student("lisi")
s2.eat()
s2.sleep()