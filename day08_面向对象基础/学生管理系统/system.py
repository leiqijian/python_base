
from student import Student

# 学生管理系统类
class StudentCMS:
    def __init__(self):
        # 学生列表 默认数据为空列表 一开始没有学生 后期逐渐加入
        self.stu_list = [
            Student("leimen", 19, "male", "110", "nice"),
            Student("Jenny", 20, "female", "119", "cool girl"),
            Student("Tom", 25, "male", "120", "Like a cat")
        ]

    def add_stu(self):
        name = input("请输入学生姓名:")
        age = eval(input("请输入学生年龄:"))
        gender = input("请输入学生性别:")
        mobile = input("请输入学生手机号:")
        desc = input("请输入学生描述:")
        self.stu_list.append(Student(name, age, gender, mobile, desc))
        print("add success")

    def del_stu(self):
        pass

    def get_stu_list(self):
        for stu in self.stu_list:
            print(stu)

    def get_single_stu(self):
        name = input("请输入需要查询的学生姓名:")
        for stu in self.stu_list:
            if stu.name == name:
                print(stu)
                break
        else:
            print("we can not find this student")


    def update_stu(self):
        name = input("请输入需要更新的学生姓名:")
        for stu in self.stu_list:
            if stu.name == name:
                stu.age = eval(input("请输入学生年龄:"))
                stu.gender = input("请输入学生性别:")
                stu.mobile = input("请输入学生手机号:")
                stu.desc = input("请输入学生描述:")
                print("update success")
                break
        else:
            print("we can not find this student")


    def save_data(self):
        with open('data.txt', "w", encoding='utf-8') as f:
            result = [stu.__dict__ for stu in self.stu_list]
            f.write( str(result) )
            print("save success")

    def show_menu(self):
        print("************************************")
        print("本学生管理系统V2.0可完成如下操作:")
        print("\t1.添加学生;")
        print("\t2.修改学生;")
        print("\t3.删除学生;")
        print("\t4.查询某个学生;")
        print("\t5.显示所有学生;")
        print("\t6.保存信息;")
        print("\t0.退出系统.")
        print("************************************")

    def start(self):
        self.load_data()
        while True:
            self.show_menu()
            # 用户输入
            num = input('请输入操作对应的数字')
            # 根据用户输入 判断各种数字 对应调用方法即可
            if num == '1':
                self.add_stu()
            elif num == '2':
                self.update_stu()
            elif num == '3':
                self.del_stu()
            elif num == '4':
                self.get_single_stu()
            elif num == '5':
                self.get_stu_list()
            elif num == '6':
                self.save_data()
            elif num == '0':
                print('再见👋🏻')
                break
            else:
                print('输入有误, 重新输入')


    def load_data(self):
        try:
            with open('data.txt', "r", encoding='utf-8') as f:
                # str ==> list ==> dict ==> object
                data = f.read()

                # print(type(temp))
                # print(temp)   #str
                # print(type(eval(temp)))
                # print(eval(temp))  #list
                # for stu in eval(temp):
                #     print(type(stu))
                #     print(stu) #dict
                #     s = Student(stu["name"], stu["age"], stu["gender"], stu["mobile"], stu["desc"])
                #     self.stu_list.append(s)

                temp = eval(data)
                result = [Student(stu["name"], stu["age"], stu["gender"], stu["mobile"], stu["desc"]) for stu in
                          temp]
                print(type(result))
                # self.stu_list = result
        except:
            pass


if __name__ == '__main__':
    sys = StudentCMS()
    # print(type(sys.stu_list))
    # print(sys.stu_list)
    # for student in sys.stu_list:
    #     print(student)
    #     print(student.__dict__)
    #     print(str(student.__dict__))
    sys.load_data()

