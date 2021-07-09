import pygame
import sounds
from KlasseMonster import Monster
from KlasseMagie import Magie
from time import time
from screen import screen

# Harpyie erbt Alles von Monster
# können den Held bei Berührung töten
# Harpyie kann in alle 4 Himmelrichtungen schießen
# Harpyie kann seitwärts schießen
# Harpyie kannn in alle Richtungen schießen

class Harpyie (Monster):                                                            #Harpyie soll in allen 4 Richtungen hin und wieder schießen
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.zeitSchuss = zeitMonster
        self.bildExplo = [pygame.image.load(f"Bilder/Magie/E1.png"),
                     pygame.image.load(f"Bilder/Magie/E2.png")]


    def faehigkeit(self):                                                    #Fähigkeiten von Monstern werden mit den Fähigkeiten der Klasse überschrieben!!!
        self.toeten()
        self.schiessen()

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.kugeln = []
        self.leben = True
        self.heldTot = False

    def schiessen(self):
        if time() - self.zeitSchuss >= 2:                                       #Schießt in alle 4 Himmelsrichtungen
            self.kugeln.append(Magie(self.x, self.y, 0, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 1, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 2, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 3, "R", 5))
            self.zeitSchuss = time()

        for k in self.kugeln:
            if self.heldDaten.rechteck.colliderect(k.kugelRec):                                  # vergleicht ob eine Kugel den Helden trifft
                sounds.soundTot()
                screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
                self.heldTot = True

            if not self.hindernis(k.kugelRec):                                                   # vergleicht ob eine Kugel ein Hindernis trifft
                self.kugeln.remove(k)

        for k in self.kugeln:                                                                     # vergleicht ob eine Kugel eine feindliche Kugel trifft
            for m in self.heldDaten.kugeln:                                                       #(zwei Schleifen hier, weil bei dem Fall wenn Hindernis und feindliche Kugel sich treffen kommt ein Fehler)
                if k.kugelRec.colliderect(m.kugelRec):
                    sounds.soundKolMag()
                    self.kugeln.remove(k)
                    self.heldDaten.kugeln.remove(m)

            k.bewegung()                                                                           # Bewegung der einzelnen Kugeln


    def schiessen_seitwaerts(self):
        if time() - self.zeitSchuss >= 2:                                       #Schießt in alle seitwaerts Richtungen
            self.kugeln.append(Magie(self.x, self.y, 4, "R", 5))                #Klasse Magie muss dafür angepasst werden
            self.kugeln.append(Magie(self.x, self.y, 5, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 6, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 7, "R", 5))
            self.zeitSchuss = time()

        for k in self.kugeln:
            if self.heldDaten.rechteck.colliderect(k.kugelRec):                                  # vergleicht ob eine Kugel den Helden trifft
                sounds.soundTot()
                screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
                self.heldTot = True

            if not self.hindernis(k.kugelRec):                                                   # vergleicht ob eine Kugel ein Hindernis trifft
                self.kugeln.remove(k)

        for k in self.kugeln:                                                                     # vergleicht ob eine Kugel eine feindliche Kugel trifft
            for m in self.heldDaten.kugeln:
                if k.kugelRec.colliderect(m.kugelRec):
                    sounds.soundKolMag()
                    self.kugeln.remove(k)
                    self.heldDaten.kugeln.remove(m)

            k.bewegung()


    def schiessen_alleRichtungen(self):
        if time() - self.zeitSchuss >= 2:                                       #Schießt in alle Richtungen
            self.kugeln.append(Magie(self.x, self.y, 0, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 1, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 2, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 3, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 4, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 5, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 6, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 7, "R", 5))
            self.zeitSchuss = time()

        for k in self.kugeln:
            if self.heldDaten.rechteck.colliderect(k.kugelRec):                                  # vergleicht ob eine Kugel den Helden trifft
                sounds.soundTot()
                screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
                self.heldTot = True

            if not self.hindernis(k.kugelRec):                                                   # vergleicht ob eine Kugel ein Hindernis trifft
                self.kugeln.remove(k)

        for k in self.kugeln:                                                                     # vergleicht ob eine Kugel eine feindliche Kugel trifft
            for m in self.heldDaten.kugeln:
                if k.kugelRec.colliderect(m.kugelRec):
                    sounds.soundKolMag()
                    self.kugeln.remove(k)
                    self.heldDaten.kugeln.remove(m)

            k.bewegung()