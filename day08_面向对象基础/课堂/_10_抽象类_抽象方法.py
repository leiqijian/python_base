'''
包含抽象方法的类，称之为抽象类。抽象方法是指：没有具体实现的方法（pass）称之为抽象方法
约束了子类必须实现某些方法，定义了子类的功能
'''
class AC():
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def r_l_wind(self):
        pass

class Media_Ac(AC):
    def cool_wind(self):
        print("media cool wind")
    def hot_wind(self):
        print("media hot wind")
    # def r_l_wind(self):
    #     print("media right left wind")

class Gree_Ac(AC):
    def cool_wind(self):
        print("Gree cool wind")
    def hot_wind(self):
        print("Gree hot wind")
    def r_l_wind(self):
        print("Gree right left wind")

def make_wind(ac : AC):
    ac.cool_wind()
    ac.hot_wind()
    ac.r_l_wind()

make_wind(Gree_Ac())
print("------")
make_wind(Media_Ac())
