import pygame
from screen import screen
from time import time
import sounds

class Magie:
    def __init__(self, spX, spY, richtung, farbe, geschw ):
        pygame.mixer.Sound.play(sounds.soundMagie())
        self.x = spX
        self.y = spY
        self.farbe = farbe
        self.richtung = richtung
        self.zeit = time()
        self.geschw = geschw
        self.kugelRec = pygame.Rect(self.x + 12 , self.y +12, 24, 24)
        self.bildbewegung = 2
        self.bildMagie = [pygame.image.load(f"Bilder/Magie/{farbe}1.png"),
                          pygame.image.load(f"Bilder/Magie/{farbe}2.png"),
                          pygame.image.load(f"Bilder/Magie/{farbe}3.png"),
                          pygame.image.load(f"Bilder/Magie/{farbe}2.png")]

        if self.richtung == 0:              #oben
            self.y -= 24

        elif self.richtung == 1:            #unten
            self.y += 24

        elif self.richtung == 2:            #rechts
             self.x += 24

        elif self.richtung == 3:            #links
            self.x -= 24


    def bewegung(self):
        if self.richtung == 0:
            self.y -= self.geschw

        elif self.richtung == 1:
            self.y += self.geschw

        elif self.richtung == 2:
            self.x += self.geschw

        elif self.richtung == 3:
            self.x -= self.geschw

        self.zeichnen()

    def zeichnen(self):

        if time() - self.zeit >= 0.2:
            self.zeit = time()
            self.bildbewegung += 1
            if self.bildbewegung >= 3:
                self.bildbewegung = 0

        screen.blit(self.bildMagie[self.bildbewegung], (self.x, self.y))
        self.kugelRec = pygame.Rect(self.x + 12, self.y +12 , 24, 24)