import pygame
from random import randint
from time import time
from KlasseFigur import Figur
from screen import screen
import sounds

# Monster erbt Alles von Figur
# Monster können selbst laufen
# Sterben, wenn sie mit der Magie des Helden in Berührung kommen
# können den Helden bei Berührung töten

class Monster(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe,level, bildFigur)
        self.xReset = x
        self.yReset = y
        self.richtung = 1
        self.zeitMonster = zeitMonster
        self.leben = True
        self.heldTot = False
        self.feuerWechsel = 0
        self.heldDaten = None
        self.monsterDaten = None

        self.platzhalter = None

        self.bildTot = [pygame.image.load(f"Bilder/Feuer/F1.png"),
                         pygame.image.load(f"Bilder/Feuer/F2.png"),
                         pygame.image.load(f"Bilder/Feuer/F3.png")]

        if bildFigur == "Harpyie" or bildFigur == "Drache":                         #Harpyien und Drachen können über Hindernisse fliegen
            self.level = 3                                                          #(Level 3 hat keine Hindernisse)

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.leben = True
        self.heldTot = False

    def mlaufen(self, spieler, monster=None):                                      #Monster können selber laufen
        if self.leben:
            self.heldDaten = spieler                                               #Alle Daten vom Held werden hier gespeichert
            self.monsterDaten = monster                                            #Alle Daten von einem Monster werden hier gespeichert



            if time() - self.zeitMonster >= 0.2:                                    # Mach draus eine nützliche Bewegungsfunktion  !!!!!
                self.zeitMonster = time()                                           # Nutze Laufen von Figur dafür       !!!!!
                self.schritt = not self.schritt                                     # Jetzt tanzen die Monster nur auf der Stelle !!!!!!
            screen.blit(self.bildUnten[self.schritt], (self.x, self.y))             #


            self.sterben()
            self.faehigkeit()
            return self.heldTot                                                     #Rückgabe ob der Held tot ist

        else:
            screen.blit(self.bildTot[self.feuerWechsel], (self.x, self.y))          #Monster brennen, wenn sie tot sind
            if time() - self.zeitMonster >= 0.1:
                if self.feuerWechsel < 2:
                    self.feuerWechsel += 1
                else:
                    self.feuerWechsel = 0
                self.zeitMonster = time()

    def toeten(self):                                                               #Held wird getötet bei Kollision
        self.platzhalter                                                            #ersetze self.platzhalter mit einem nützlichen code

    def sterben(self):                                                              #Monster ist tot nach der Berührung von der Magie des Helden
        self.platzhalter                                                            #ersetze self.platzhalter mit einem nützlichen code

    def faehigkeit(self):                                                           #Alle Fähigkeiten von Monster kommen hier rein
        self.toeten()