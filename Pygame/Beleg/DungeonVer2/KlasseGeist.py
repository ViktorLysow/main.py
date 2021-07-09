import pygame
from KlasseMonster import Monster
from time import time
from random import randint
from screen import screen



class Geist (Monster):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.dupliList = []
        self.zeitDupl = zeitMonster
        self.anzahlDouble = 1


    def mLaufen(self, spieler):  # Monster können selber laufen
        self.heldDaten = spieler
        if time() - self.zeitMonster >= 1:  # abhängig von der zeit
            self.richtung = randint(0, 3)
            self.zeitMonster = time()
        self.laufen(self.richtung)
        for i in self.dupliList:
            if i.laufen(self.heldDaten):
                return True
        self.duplizieren()

        if self.anzahlDouble >= 3:
            print('hallo')
            self.kill()

        return self.toeten()

    def toeten(self):
        if self.rechteck.colliderect(self.heldDaten.rechteck):
            screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
            return True

    def duplizieren(self):
        global anzahl
        if self.anzahlDouble >= 4:
            self.zeitDupl = 0

        if time() - self.zeitDupl >= 2*self.anzahlDouble:
            self.dupliList.append(Monster(self.x, self.y, self.geschw, self.breite, self.hoehe, self.level, self.bildFigur, time()))
            self.zeitDupl = time()
            self.anzahlDouble += 1