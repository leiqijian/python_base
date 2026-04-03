'''
- 1.创建一个动物(Animal)的基类，其中有一个run方法, 输出`跑起来....`
- 2.创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
  - 2.1 run方法输出 `跑起来....`
  - 2.2 eat 方法输出 `吃东西...`
- 3.创建一个 SwiftHorse（千里马）类继承Horse类，初始化init方法name属性为千里马，同时针对吃东西，SwiftHorse类中重写eat方法，增加打印输出"`一天可以吃一担粮食...`"
'''


class Animal:
    def run(self):
        print("RUN")

class Horse(Animal):
    def run(self):
        print("跑起来....")

    def eat(self):
        print("吃东西...")

class SwiftHorse(Horse):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}一天可以吃一担粮食...")

if __name__ == '__main__':
    H1 = SwiftHorse("swift horse")
    H1.run()
    H1.eat()