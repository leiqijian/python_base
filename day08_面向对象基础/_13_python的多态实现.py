'''
同一个函数随着传入子类对象不同，可以返回不同的结果
好处：提高程序的可扩展性，解耦合（可以把复杂的系统拆解为若干个独立的小模块），额外增加一个功能的时候对原有的框架基本没有影响，利于业务发展
'''
'''
首先定义一个父类，其可能拥有多个子类对象。当我们调用一个公共方法（接口）时，传递的对象不同，则返回的结果不同。
'''
class Fruit(object):
    def makejuice(self):
        print('i can make juice')

class Apple(Fruit):
    # 重写父类方法
    def makejuice(self):
        print('i can make apple juice')

class Banana(Fruit):
    # 重写父类方法
    def makejuice(self):
        print('i can make banana juice')

class Orange(Fruit):
    # 重写父类方法
    def makejuice(self):
        print('i can make orange juice')

# 定义一个公共接口（专门用于实现榨汁操作）
def service(Fruit):
    # obj要求是一个实例化对象，可以传入苹果对象/香蕉对象
    Fruit.makejuice()

# 调用公共方法
service(Orange())

print("-------------------")


class Animal():
    def speak(self):
        pass

class Dog(Animal):
     def speak(self):
         print('wangwangwang')


class Cat(Animal):
    def speak(self):
        print('miaomiaomiao')

class Person(Animal):
    def speak(self):
        print('hello')

class Car():
    def speak(self):
        print('dididi')

class Bus():
    def __init__(self, fn):
        self.fn = fn


def make_noice(a : Animal):
    a.speak()

# make_noice(Dog())
# make_noice(Cat())
# make_noice(Person())
# make_noice(Car())  #python中的伪多态，只要传入的对象有speak方法，就可以调用

# def speak():
#     pass
# make_noice(Bus(speak()))

print("---------*******----------")

def a():
    print("Bus is making noise!")

class Bus():
    def __init__(self, fn):
        self.speak = fn
        print(f"aaa{self.speak}aaa")
        print(f"bbb{self.speak()}bbb")

def make_noice(a : Animal):
    a.speak()

bus = Bus(a)
make_noice(bus)   #Bus is making noise!