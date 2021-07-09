import pygame
from screen import screen
from KlasseFigur import Figur


class Held(Figur):
    def __init__(self, x, y, geschw, breite, level, hoehe, bildFigur):
        super().__init__(x, y, geschw, breite, level, hoehe, bildFigur)
        self.bildOben.append(pygame.image.load(f"Bilder/{bildFigur}/HintenS.png"))
        self.bildUnten.append(pygame.image.load(f"Bilder/{bildFigur}/VornS.png"))
        self.bildRechts.append(pygame.image.load(f"Bilder/{bildFigur}/RechtsS.png"))
        self.bildLinks.append(pygame.image.load(f"Bilder/{bildFigur}/LinksS.png"))
        self.bildtot = pygame.image.load(f"Bilder/{bildFigur}/tot.png")
        self.stehRicht = 0

    def stehen(self):                                                                           #Nur der held kann stehen
        if self.stehRicht == 0:
            screen.blit(self.bildOben[2], (self.x, self.y))
        if self.stehRicht == 1:
            screen.blit(self.bildUnten[2], (self.x, self.y))
        if self.stehRicht == 2:
            screen.blit(self.bildRechts[2], (self.x, self.y))
        if self.stehRicht == 3:
            screen.blit(self.bildLinks[2], (self.x, self.y))

    def sterben(self,monster):                                                 #zur zeit stirbt nur der Held bei berührung mit Monstern
        if self.rechteck.colliderect(monster):
            screen.blit(self.bildtot, (self.x, self.y))
            return True

    def steurung(self):
        self.gedrueckt = pygame.key.get_pressed()
        if self.gedrueckt[pygame.K_UP]:
            self.laufen(0)
            self.stehRicht = 0
        elif self.gedrueckt[pygame.K_DOWN]:
            self.laufen(1)
            self.stehRicht = 1
        elif self.gedrueckt[pygame.K_RIGHT]:
            self.laufen(2)
            self.stehRicht = 2
        elif self.gedrueckt[pygame.K_LEFT]:
            self.laufen(3)
            self.stehRicht = 3
        else:
            self.stehen()