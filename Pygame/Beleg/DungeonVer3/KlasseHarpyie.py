import pygame
import sounds
from KlasseMonster import Monster
from KlasseMagie import Magie
from time import time
from hindernise import grenzeLevel
from screen import screen


class Harpyie (Monster):                                                            #Harpyie soll in allen 4 Richtungen hin und wieder schißen
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.zeitSchuss = zeitMonster
        self.bildExplo = [pygame.image.load(f"Bilder/Magie/E1.png"),
                     pygame.image.load(f"Bilder/Magie/E2.png")]


    def hindernis(self,richtung):                                                   #kann über Lava fliegen
        r = True
        for i in grenzeLevel[2]:
            if richtung.colliderect(i):
                r = False
        return r

    def fähigkeit(self):
        self.schissen()

    def schissen(self):
        if time() - self.zeitSchuss >= 2:
            self.kugeln.append(Magie(self.x, self.y, 0, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 1, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 2, "R", 5))
            self.kugeln.append(Magie(self.x, self.y, 3, "R", 5))
            self.zeitSchuss = time()

        for k in self.kugeln:
            if self.heldDaten.rechteck.colliderect(k.kugelRec):
                pygame.mixer.Sound.play(sounds.soundTot())
                screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
                self.heldTot = True

            if not self.hindernis(k.kugelRec):
                self.kugeln.remove(k)

            for m in self.heldDaten.kugeln:
                if k.kugelRec.colliderect(m.kugelRec):
                    pygame.mixer.Sound.play(sounds.soundKolMag())
                    #screen.blit(self.bildExplo[0], (k.x, k.y))
                    #pygame.display.update()
                    self.kugeln.remove(k)
                    self.heldDaten.kugeln.remove(m)

            k.bewegung()