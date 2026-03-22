# 案例：定义一个Girl类，拥有两个属性name和age，将age设置为私有属性。

class Girl():

    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __showinfo(self):
        print('姓名：%s，年龄：%d' % (self.name, self.__age))


g1 = Girl('Jenny')
