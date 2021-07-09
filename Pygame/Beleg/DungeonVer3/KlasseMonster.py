import pygame
from random import randint
from time import time
from KlasseFigur import Figur
from screen import screen
import sounds

class Monster(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe,level, bildFigur)
        self.xReset = x
        self.yReset = y
        self.richtung = 1
        self.zeitMonster = zeitMonster
        self.Leben = True
        self.heldTot = False
        self.lichtWechsel = 0
        self.heldDaten = None

        self.bildTot = [pygame.image.load(f"Bilder/Licht/L1.png"),
                         pygame.image.load(f"Bilder/Licht/L2.png"),
                         pygame.image.load(f"Bilder/Licht/L3.png")]


    def mLaufen(self, spieler):                                                 #Monster können selber laufen
        if self.Leben:
            self.heldDaten = spieler
            if time() - self.zeitMonster >= 1:                                     #abhängig von der zeit
                self.richtung = randint(0, 3)
                self.zeitMonster = time()
            self.laufen(self.richtung)
            self.fähigkeit()
            self.toeten()
            self.sterben()
            return self.heldTot

        else:
            screen.blit(self.bildTot[self.lichtWechsel], (self.x, self.y))
            if time() - self.zeitMonster >= 0.15:
                if self.lichtWechsel < 2:
                    self.lichtWechsel += 1
                else:
                    self.lichtWechsel = 0
                self.zeitMonster = time()


    def toeten(self):
        if self.rechteck.colliderect(self.heldDaten.rechteck):
            pygame.mixer.Sound.play(sounds.soundTot())
            screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
            self.heldTot = True

    def sterben(self):
        for k in self.heldDaten.kugeln:
            if self.rechteck.colliderect(k.kugelRec):
                self.heldDaten.kugeln.remove(k)
                self.Leben = False
                pygame.mixer.Sound.play(sounds.soundFeuer())

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.kugeln = []
        self.Leben = True
        self.heldTot = False

    def fähigkeit(self):
        self.nichts = None