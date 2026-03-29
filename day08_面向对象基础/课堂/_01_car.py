
# class Car():
#     def run(self):
#         print("this car can run")
#
# c1 = Car()
# c1.run()


class Student():
    def homework(self):
        print("homework")
        print(self) #0x000002508BCA7230

s1 = Student()
print("-------")
print(s1)  #0x000002508BCA7230
print("-------")
s1.homework()
