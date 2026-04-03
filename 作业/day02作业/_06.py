'''
国家部门制定了打印机标准
1、请抽象父类，制定标准：抽象printer，要求支持黑白打印(Black_white_printing)、彩色打印(color_printing)。
2、完成打印机hp、小米、佳能（canon）硬件入围；入围测试平台 make_test_printing(myobj:抽象类))
3、完成多态场景测试
'''

class Printer(object):
    def Black_white_printing(self):
        pass
    def color_printing(self):
        pass

class hp_printer(Printer):
    def Black_white_printing(self):
        print("hp_black_white_printing")
    def color_printing(self):
        print("hp_color_printing")


class xiaomi(Printer):
    def Black_white_printing(self):
        print("xiaomi_black_white_printing")
    def color_printing(self):
        print("xiaomi_color_printing")

class canon(Printer):
    def Black_white_printing(self):
        print("canon_black_white_printing")

    def color_printing(self):
        print("canon_color_printing")


def make_test_printing(Printer):
    Printer.Black_white_printing()
    Printer.color_printing()


if __name__ == '__main__':
    hp = hp_printer()
    xiaomi = xiaomi()
    canon = canon()

    make_test_printing(hp)
    print("-----")
    make_test_printing(xiaomi)
    print("-----")
    make_test_printing(canon)

