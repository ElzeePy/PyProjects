import random


class Player:
    def __init__(self,hp,mp,atkl,atkh):
        self.maxhp = hp
        self.maxmp = mp
        self.hp = hp
        self.mp = mp
        self.atkl = atkl
        self.atkh = atkh


    def getPlayerDMG(self):
        dmg = random.randint(self.atkl,self.atkh)
        return dmg

    def getPlayerHP(self):
        return self.hp

    def getPlayerMP(self):
        return self.mp

    def getPlayerPower(self):
        return (self.atkh+self.atkl)/2










