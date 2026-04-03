'''
构建对象对战平台object_play
1 英雄一代战机（战斗力60）与敌军战机（战斗力70）对抗。英雄1代战机失败！
2 卧薪尝胆，英雄二代战机（战斗力80）出场！，战胜敌军战机！
3 对象对战平台object_play, 代码不发生变化的情况下, 完成多次战斗
'''
class Hero(object):
    def power(self):
        return 60

class Hero2(Hero):
    def power(self):
        return 80

class Enemy(object):
    def power(self):
        return 70

def fight(Hero, Enemy):
    if  Hero.power() < Enemy.power():
        print("fail")
    elif Hero.power() > Enemy.power():
        print("success")
    else:
        print("==")

if __name__ == '__main__':
    H1 = Hero()
    H2 = Hero2()
    E1 = Enemy()
    fight(H1, E1)
    fight(H2, E1)


