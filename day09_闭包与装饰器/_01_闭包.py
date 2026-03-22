'''
1. 有嵌套
2. 有引用
3. 有返回

闭包的作用：在整体函数结束之后，内部的变量不会被系统所回收
'''
def outer():

    number = 10

    def inner():

        print(number)

    return inner  #outer函数的返回 不能有括号

func = outer() #相当于返回了inner这个函数的对象地址
print(func)
func() #相当于调用了inner（）函数
