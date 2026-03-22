'''
虽然python支持多继承，但是如果多个父类中存在相同的方法，子类是如何继承的呢
'''

class A(object):
    def eat(self):
        print("A eat method")

class B(object):
    def eat(self):
        print("B eat method")

class C(A, B):
    pass

c = C()
c.eat() #A eat method
print(C.mro())  #[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]