'''
super()
当子类继承了父类，同事重写父类中的方法，这个时候如果需要在子类中访问父类中被重写的方法，就可以使用super（）
'''

class Car(object):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('i can run')


class GasolineCar(Car):
    def run(self):
        print('i can run with gasoline')


class ElectricCar(Car):
    def __init__(self, brand, model, color, battery):  #子类中特有的构造方法
        super().__init__(brand, model, color)  #引用父类的构造方法
        # 电池属性
        self.battery = battery

    def run(self):
        print(f'i can run with electric，i have a {self.battery} + "kwh battery"')


bwm = GasolineCar('宝马', 'X5', '白色')
bwm.run()

tesla = ElectricCar('特斯拉', 'Model S', '红色', 70)
tesla.run()