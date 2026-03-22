'''
global: 声明全局变量
nonlocal: 只能应用于嵌套函数，用于访问嵌套函数中的局部变量
一个函数嵌套了另一个函数，在内层函数中是否可以修改上一层的局部变量呢，默认是不可以
但是可以通过nonlocal关键字，在嵌套的前提下，让我们在函数内部声明外部的局部变量
'''

def outer():
    number = 10

    def inner():
        nonlocal number
        number = 100
    inner()
    print(number)

#调用outer函数
outer()
