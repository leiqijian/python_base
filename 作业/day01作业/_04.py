'''
减肥案例
'''


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 2

    def eat(self):
        self.weight += 5

    def __str__(self):
        return f"{self.name}, weight: {self.weight}"

if __name__ == '__main__':
    p1 = Person("leimen", 100)
    p1.run()
    p1.run()
    p1.run()
    p1.eat()
    p1.eat()
    p1.eat()
    print(p1)