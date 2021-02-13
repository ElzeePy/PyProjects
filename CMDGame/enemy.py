import random


class Enemy:
    def __init__(self,hp,mp,atkl,atkh):
        self.hp = hp
        self.mp = mp
        self.atkl = atkl
        self.atkh = atkh

    def getEnemyDMG(self):
        dmg = random.randint(self.atkl,self.atkh)
        return dmg

    def getEnemyHP(self):
        return self.hp

    def getEnemyMP(self):
        return self.mp

    def getEnemyPower(self):
        return (self.atkh+self.atkl)/2








