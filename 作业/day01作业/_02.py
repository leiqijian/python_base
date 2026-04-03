'''
定义一个电脑类，并给电脑添加品牌、价格等属性，同时电脑能用于编程、看视频。
'''

class Computer(object):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def coding(self):
        print(f"{self.brand} PC can coding")

    def watch_video(self):
        print(f"{self.brand} PC can watch video")

if __name__ == '__main__':
    c1 = Computer("Apple", 100)
    c1.coding()
    c1.watch_video()


