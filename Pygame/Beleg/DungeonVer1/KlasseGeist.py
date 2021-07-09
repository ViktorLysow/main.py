from KlasseMonster import Monster
from time import time
from random import randint

anzahl = 1

class Geist (Monster):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.dupli = []
        self.zeitDupl = zeitMonster


    def mLaufen(self):  # Monster können selber laufen
        if time() - self.zeitMonster >= 1:  # abhängig von der zeit
            self.richtung = randint(0, 3)
            self.zeitMonster = time()
        self.laufen(self.richtung)

        for i in self.dupli:
            i.laufen()

        self.duplizieren()


    def duplizieren(self):
        global anzahl
        if time() - self.zeitDupl >= 5:
            self.dupli.append(Geist(self.x,self.y,self.geschw,self.breite,self.hoehe,self.level,self.bildFigur,time()))
            self.zeitDupl = time()
            anzahl += 1
            print(anzahl)