'''
类方法就是针对类对象定义的方法，在方法中可以直接访问类属性或者调用其他类方法
'''

class Dog:
    #@staticmethod表示方法是一个静态方法，属于类本身
    #使用 类.静态方法名 调用
    #静态方法没有参数，适合一些跟类没有太大关系的方法
    @staticmethod
    def sleep():
        print("sleep")


    #@classmethod表示方法是一个类方法，属于类本身
    #使用 类.类方法名 调用
    #类方法有参数，适合一些跟类有关的方法，可以通过cls参数获得一些类的信息
    @classmethod
    def eat(cls):
        print("eat")

    #该方法是实例方法，是对象方法，需要通过对象调用
    def drink(self):
        print("drink")
    
dog = Dog()
dog.drink()
Dog.eat()
Dog.sleep()