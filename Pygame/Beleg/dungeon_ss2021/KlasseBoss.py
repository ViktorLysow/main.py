# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Boss-Klasse
# Autor: Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Boss-Entität definieren
# 
# Klasse Boss erbt alles von Geist
# kann in vier Richtungen schießen

from KlasseGeist import Geist
from KlasseMagie import Magie
import sounds
from time import time
from screen import screen


class Boss (Geist):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.zeitSchuss = zeitMonster

    def faehigkeit(self):  # Fähigkeiten von Monstern werden mit den Fähigkeiten der Klasse überschrieben!!!
        self.toeten()
        self.schiessen()
        self.duplizieren()

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.kugeln = []
        self.leben = True
        self.heldTot = False
        self.anzahlDouble = 1
        self.dupliList = []

    def schiessen(self):
        if time() - self.zeitSchuss >= 2:  # Schießt in alle 4 Himmelsrichtungen
            self.kugeln.append(Magie(self.x, self.y, 0, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 1, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 2, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 3, "R", 5))
            self.zeitSchuss = time()

        for k in self.kugeln:
            if self.heldDaten.rechteck.colliderect(k.kugelRec):  # vergleicht ob eine Kugel den Helden trifft
                sounds.soundTot()
                screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
                self.heldTot = True

            if not self.hindernis(k.kugelRec):  # vergleicht ob eine Kugel ein Hindernis trifft
                self.kugeln.remove(k)

        for k in self.kugeln:  # vergleicht ob eine Kugel eine feindliche Kugel trifft
            for m in self.heldDaten.kugeln:  # (zwei Schleifen hier, weil bei dem Fall wenn Hindernis und feindliche Kugel sich treffen kommt ein Fehler)
                if k.kugelRec.colliderect(m.kugelRec):
                    sounds.soundKolMag()
                    self.kugeln.remove(k)
                    self.heldDaten.kugeln.remove(m)

            k.bewegung()