'''
烤地瓜案例
'''

class potato(object):
    def __init__(self,condiment = [], cook_time=0):
        #initial
        self.status = "生的"
        self.condiment = condiment
        self.cook_time = cook_time

    def add_condiment(self, condiment):
        self.condiment.append(condiment)

    def cook(self, cook_time):
        self.cook_time += cook_time

    def __str__(self):
        print(self.cook_time)
        if 0 <= self.cook_time < 3:
            self.status = '生的'
        elif 3 <= self.cook_time < 7:
            self.status = "半生不熟"
        elif 7 <= self.cook_time < 12:
            self.status = "熟了"
        else:
            self.status = "烤焦了"

        return f"potato status is {self.status}, already cooking {self.cook_time} minutes, with {self.condiment}"

if __name__ == '__main__':
    p1 = potato()
    p2 = potato("榴莲", cook_time=10)
    print(p1)
    print(p2)
    p2.cook(cook_time=3)
    print(p2)