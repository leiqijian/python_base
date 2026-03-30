class Student(object):
    def __init__(self, name, age, gender, mobile, desc):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.desc = desc

    def __str__(self):
        return f"name:{self.name}, age: {self.age}, gender: {self.gender}, mobile: {self.mobile}, desc: {self.desc}"

'''
__name__ 当前文件运行的时候输出__main__，被其他文件调用的时候，显示这个文件的文件名。所以该类的测试代码写在当前类的if __name__ == '__main__':里面
'''
# print(__name__) # '__main__'
if __name__ == '__main__':
    s1 = Student("leimen", 19, "male", "110", "nice")
    print(s1)