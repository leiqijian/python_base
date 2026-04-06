class Person:
    def __init__(self):
        self.__age= 1

    @property
    def age(self):     #使用@property 把方法改成属性的方式获取age
        return self.__age

    @age.setter
    def age(self,new_age):      #使用@方法名.setter 把设置age的方法变成能属性赋值的方式去设值。方法名需要跟获取方法名一致
        self.__age = new_age

p1 = Person()
print(p1.age)
p1.age=2
print(p1.age)

