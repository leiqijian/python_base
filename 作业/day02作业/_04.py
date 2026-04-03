'''
综合训练：
定义一个`Person` 类,包含初始化 init 方法:
实例属性:       名字, name 年龄, age
1. 记录由该类创建的对象的个数，创建一个对象，计数+1，删除一个对象，计数-1；
2. 定义一个方法，可以打印当前对象的个数；
3. 定义一个方法`show_info`, 输出以下信息
   这是一个 Person 类,谢谢查看!
4. 打印对象的时候，可以输出打印自己的名字和年龄
   我的名字是 xxx, 年龄是 xxx
5. 定义一个方法 `study`, 输出以下信息
   我叫 xxx, 我要好好学习
6. 操作步骤
   1.  调用`show_info `方法；
   2.  创建两个对象, 打印当前对象，并打印当前的对象个数；
   3.  分别使用两个对象调用`study`方法；
   4.  删除一个对象，打印输出当前的对象个数。
'''

class Person():
    count = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.count += 1

    def __del__(self):
        Person.count -= 1

    def __str__(self):
        return "我的名字是{}, 年龄是{}".format(self.name,self.age)

    def show_count(self):
        return Person.count

    def show_info(self):
        print("这是一个 Person 类,谢谢查看!")

    def study(self):
        print("我叫{}， 我要好好学习".format(self.name))


if __name__ == '__main__':
    P1 = Person("Leimen", 20)
    P1.show_info()

    P2 = Person("Jenny", 30)
    print(P2)
    print(P1)
    print(Person.count)

P2.__del__()
print(Person.count)



