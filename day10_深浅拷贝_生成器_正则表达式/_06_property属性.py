class Person:
    def __init__(self):
        self.__age= 1

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age = new_age

    age = property(get_age,set_age)

p1 = Person()
print(p1.age)
p1.age=2
print(p1.age)

