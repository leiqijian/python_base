'''
实操练习：

- 1.创建一个Animal（动物）基类，其中有一个run方法，输出`跑起来....`；

- 2.创建一个Horse（马）类继承于动物类，Horse类中不仅有run()方法还有eat()方法；
- 2.1run方法输出 `跑起来....`

- 2.2 eat 方法输出 `吃东西...`
'''

class Animal:
    def run(self):
        print("RUN")

class Horse(Animal):
    def run(self):
        print("HORSE RUN")

    def eat(self):
        print("HORSE EAT")

if __name__ == '__main__':
    H1 = Horse()
    H1.run()
    H1.eat()