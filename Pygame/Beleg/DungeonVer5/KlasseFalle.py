import pygame
from screen import screen
from time import time
import sounds

class Falle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heldDaten = None
        self.warte = False
        self.zeit = time()
        self.FalleRec = pygame.Rect(self.x +12, self.y +12, 24, 24)              #Rechteck ist halb so groß
        self.bildbewegung = 0
        self.bildFalle = [pygame.image.load(f"Bilder/Falle/Falle1.png"),
                          pygame.image.load(f"Bilder/Falle/Falle2.png"),
                          pygame.image.load(f"Bilder/Falle/Falle3.png"),
                          pygame.image.load(f"Bilder/Falle/Falle4.png"),
                          pygame.image.load(f"Bilder/Falle/Falle3.png"),
                          pygame.image.load(f"Bilder/Falle/Falle2.png")]


    def bewegung(self, spieler):
        self.heldDaten = spieler
        if self.warte or time() - self.zeit >= 3:                                                           #3 Sekunden lang bewegt sich die Falle nicht
            self.warte = True
            if time() - self.zeit >= 0.1:                                                                   #Alle 0.1 Sekunden bewegt sich die Falle
                self.zeit = time()
                self.bildbewegung += 1
                if self.bildbewegung == 3:
                    if self.heldDaten.rechteck.colliderect(self.FalleRec):                                  #Prüfen ob ausgelöste Falle den Helden berührt
                        screen.blit(self.bildFalle[self.bildbewegung], (self.x, self.y))                    #Bild von Falle
                        screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))           #Bild vom Toten Held
                        sounds.soundTot()
                        return True
                elif self.bildbewegung >= 6:
                    self.bildbewegung = 0
                    self.warte = False

        screen.blit(self.bildFalle[self.bildbewegung], (self.x, self.y))
        return False

