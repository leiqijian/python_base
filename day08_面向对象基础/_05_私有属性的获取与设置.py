class Person:
    def __init__(self):
        self.__age = 18
        self.__name = 'tom'

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person()
print(p1.get_age())
p1.set_age(20)
print(p1.get_age())
