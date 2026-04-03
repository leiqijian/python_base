'''
定义一个手机类，能开机、能关机、可以拍照。
'''


class Phone():
    def open(self):
        print("开机")

    def close(self):
        print("关机")

    def take_photo(self):
        print("拍照")

if __name__ == "__main__":
    p1 = Phone()
    p1.open()
    p1.close()
    p1.take_photo()
