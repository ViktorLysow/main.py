from KlasseMonster import Monster
from time import time
from random import randint
from screen import screen



class Geist (Monster):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.MonsterDupl = Monster
        self.dupliList = []
        self.zeitDupl = zeitMonster
        self.anzahlDouble = 1



    def fähigkeit(self):
        self.toeten()
        self.duplizieren()

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.Leben = True
        self.heldTot = False
        self.anzahlDouble = 1
        self.dupliList = []

    def duplizieren(self):
        for i in self.dupliList:
            if i.mlaufen(self.heldDaten):
                self.heldTot = True
        if time() - self.zeitDupl >= 0.5*self.anzahlDouble:
            self.dupliList.append(self.MonsterDupl(self.x, self.y, self.geschw, self.breite, self.hoehe, self.level, self.bildFigur, time()))
            self.zeitDupl = time()
            self.anzahlDouble += 1