class Master():
    def __init__(self):
        skill = "[old cooking]"
        self.skill = skill

    def make_cake(self):
        print(f"I {self.skill} cook a old cake")

class Prentice(Master):
    def __init__(self):
        skill = "[self cooking]"
        self.skill = skill

    def make_cake(self):
        print(f"I {self.skill} cook a self cake")

    def make_master_cake(self):
        #子类调用父类方法
        # Master.__init__(self)
        # Master.make_cake(self)
        # Master().__init__(self)         # 错误写法
        # Master().make_cake(self)        # 错误写法
        super().__init__()
        super().make_cake()
        # super.__init__()                # 错误写法
        # super.make_cake()               # 错误写法

p1 = Prentice()
p1.make_master_cake()