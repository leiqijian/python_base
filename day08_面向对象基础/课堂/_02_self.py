class Car():
    def fire(self):
        print("点火")
    def check_wheel(self):
        print("检查轮胎")
    def check_oil(self):
        print("检查汽油")

    def start(self):

        self.check_wheel()
        self.check_oil()
        self.fire()
        print("启动成功")

c1 = Car()
c1.start()

