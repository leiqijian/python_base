'''
尝试定义一个算法工程师类，同时使用`__init__()`初始化岗位名称、薪资金额等属性，工作内容是每天码代码，同时使用`__str__()`展示对象所拥有的所有信息。
'''

class Engineer(object):
    def __init__(self, post, salary, job):
        self.post = post
        self.salary = salary
        self.job = job

    def __str__(self):
        return f"岗位： {self.post}， 工资：{self.salary}， 工作内容：{self.job}"

if __name__ == '__main__':
    e1 = Engineer("AI 算法工程师", 30000, "做牛做马")
    print(e1)

