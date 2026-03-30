class Master():
    def __init__(self):
        skill = "[old cooking]"
        self.skill = skill

    def make_cake(self):
        print(f"I {self.skill} cook a old cake")

class School():
    def __init__(self):
        skill = "[new cooking]"
        self.skill = skill

    def make_cake(self):
        print(f"I {self.skill} cook a new cake")

class Prentice(School, Master):
    def __init__(self):
        skill = "[self cooking]"
        self.skill = skill

    def make_cake(self):
        print(f"I {self.skill} cook a self cake")


#
# m1 = Master()
# print(m1.skill)
# m1.make_cake()
print("-----*******-------")
# s1 = School()
# print(s1.skill)
# s1.make_cake()
print("------******------")
p1 = Prentice("leimen", 20)
print(p1.skill)
p1.make_cake()
print(p1.get_name())
print(p1.get_age())

#[<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>]\
print(Prentice.__mro__)
print(Prentice.mro())
