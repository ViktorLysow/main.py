from random import randint
from time import time
from KlasseFigur import Figur

class Monster(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe,level, bildFigur)
        self.richtung = 1
        self.zeitMonster = zeitMonster

    def mLaufen(self):                                                         #Monster können selber laufen
        if time() - self.zeitMonster >= 1:                                     #abhängig von der zeit
            self.richtung = randint(0, 3)
            self.zeitMonster = time()
        self.laufen(self.richtung)