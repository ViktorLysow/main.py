import pygame
from KlasseMonster import Monster
from time import time
from random import randint

# Geist erbt alles von Monster
# können den Held bei Berührung töten
# Geist kann neue Monster erschaffen, die wie Geister aussehen
# Geist kann kurz zeitig unsichtbar werden
# Geist kannn sich teleportieren

class Geist (Monster):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.MonsterDupl = Monster                                                              #Welche Klasse erschaffen wird
        self.dupliList = []                                                                     #Liste der erschaffenen Monster
        self.zeitDupl = zeitMonster
        self.anzahlDouble = 1

        self.zeitUnsicht = zeitMonster
        self.bildUnsicht = [pygame.image.load("Bilder/Geist/tot.png"),
                         pygame.image.load("Bilder/Geist/tot.png")]
        self.saveBildOben = self.bildOben
        self.saveBildUnten = self.bildUnten
        self.saveBildRechts = self.bildRechts
        self.saveBildLinks = self.bildLinks

        self.zeitSpring = zeitMonster

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.leben = True
        self.heldTot = False
        self.anzahlDouble = 1
        self.dupliList = []


    def faehigkeit(self):                        #Fähigkeiten von Monstern werden mit den Fähigkeiten der Klasse überschrieben!!!
        self.toeten()
        self.duplizieren()
        #self.unsichtbar()
        #self.springen()


    #Alle Fähigkeiten der Klasse Geist

    def duplizieren(self):
        for dupli in self.dupliList:                                                            #Alle erschaffenen Monster in Bewegung bringen
           if dupli.mlaufen(self.heldDaten):                                                    #Prüfen ob ein erschaffenes Monster den Held getötet hat
                self.heldTot = True

        if time() - self.zeitDupl >= 0.5 * self.anzahlDouble:                                   #Zeit zur Duplezierung wird jedes mal erhöht
            self.dupliList.append(self.MonsterDupl(self.x, self.y, self.geschw, self.breite, self.hoehe, self.level, self.bildFigur, time())) #Monster wird erschaffen und in die Liste eingefügt
            self.zeitDupl = time()                                                                                                            #Zeit wird wieder auf Null gesetzt
            self.anzahlDouble += 1


    def unsichtbar(self):
        if time() - self.zeitUnsicht >= 5:          #Bilder werden umgetauscht
            self.bildOben = self.bildUnsicht
            self.bildUnten = self.bildUnsicht
            self.bildRechts = self.bildUnsicht
            self.bildLinks = self.bildUnsicht

            if time() - self.zeitUnsicht >= 10:
                self.bildOben = self.saveBildOben
                self.bildUnten = self.saveBildUnten
                self.bildRechts = self.saveBildRechts
                self.bildLinks = self.saveBildLinks

                self.zeitUnsicht = time()


    def springen(self):
        if time() - self.zeitSpring >= 5:
            self.zeitSpring = time()
            while True:
                self.x = randint(49, 768)
                self.y = randint(49, 576)
                self.rechteck = pygame.Rect(self.x, self.y, self.breite, self.hoehe)
                if self.hindernis(self.rechteck) and not self.rechteck.colliderect(self.heldDaten.rechteck):    #Prüfen, dass der Geist mit Nichts kollidiert
                    break