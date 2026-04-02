import random

def fun():
    try:
        with open('data.txt', "r", encoding='utf-8') as f:
            data = f.read()
            list = data.split("\n")
            random_num = random.randint(0, len(list) - 1)
            return list[random_num]
    except:
        pass



if __name__ == '__main__':
    name = fun()
    print(name)