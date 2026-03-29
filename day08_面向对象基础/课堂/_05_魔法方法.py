# __init__
#__str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

    def __del__(self):
        print("del function is working")

p1 = Person("leimen", 20)
p1.eat()
p1.sleep()

print("1111")
print(p1)

print("222")
del p1
print(p1)





