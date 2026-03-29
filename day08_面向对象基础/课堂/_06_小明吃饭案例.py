class Student:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def __str__(self):
        return f"{self.name} is {self.age} years old, weight is {self.weight}"
    def run(self):
        self.weight -= 0.5
    def eat(self):
        self.weight += 2

s1 = Student(age= 10, weight= 50, name= "leimen")
s1.run()
s1.run()
s1.run()
s1.run()
print(s1)
s1.eat()
s1.eat()
s1.eat()
print(s1)


