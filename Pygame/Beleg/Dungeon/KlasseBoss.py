import pygame
from KlasseGeist import Geist
from KlasseHarpyie import Harpyie
from KlasseFalle import Falle
import sounds
from time import time
from random import randint

# Klasse Monster erbt alles von Geist und Harpyie
# kann direkt unter dem Helden Fallen legen

class Boss (Geist, Harpyie):       #Boss soll alle Monster fähigkeiten haben + vielleicht noch eine
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur,zeitMonster)
        self.MonsterDupl = Harpyie                                                          #Boss dupliziert Harpyen, die wie er aussehen
        self.Falle = None

    def faehigkeit(self):                                                                    #Fähigkeiten von Monster werden mit den Fähigkeiten der Klasse überschrieben!!!
        if not self.leben:                                                                  #Besonderer Sound beim Töten vom Boss
            sounds.soundGewonne()
        self.toeten()
        self.duplizieren()
        self.schiessen()
        self.fallenLegen()

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.kugeln = []
        self.anzahlDouble = 1
        self.dupliList = []
        self.leben = True
        self.heldTot = False


    def fallenLegen(self):
        if time() - self.zeitSpring >= 4:
            self.zeitSpring = time()
            self.Falle = Falle(self.heldDaten.x, self.heldDaten.y)
        if self.Falle.bewegung(self.heldDaten):
            self.heldTot = True