import pygame
from random import randint
from time import time
from KlasseFigur import Figur
from screen import screen

class Monster(Figur, pygame.sprite.Sprite):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe,level, bildFigur)
        pygame.sprite.Sprite.__init__(self)
        self.richtung = 1
        self.zeitMonster = zeitMonster
        self.heldDaten = None

    def mLaufen(self, spieler):                                                 #Monster können selber laufen
        self.heldDaten = spieler
        if time() - self.zeitMonster >= 1:                                     #abhängig von der zeit
            self.richtung = randint(0, 3)
            self.zeitMonster = time()
        self.laufen(self.richtung)
        return self.toeten()

    def toeten(self):
        if self.rechteck.colliderect(self.heldDaten.rechteck):
            screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
            return True

    def sterben(self):
        self.kill()
