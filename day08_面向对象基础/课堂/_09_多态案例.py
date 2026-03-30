class HeroFighter():
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

class EnemyFighter():
    def attach(self):
        return 70

def object_play(a : HeroFighter , b : EnemyFighter):
    if a.power() > b.attach():
        print("win")
    elif a.power() == b.attach():
        print("nothing happened")
    else:
        print("lose")

h1 = HeroFighter()
h2 = AdvHeroFighter()
e1 = EnemyFighter()
object_play(h1,e1)
object_play(h2,e1)
