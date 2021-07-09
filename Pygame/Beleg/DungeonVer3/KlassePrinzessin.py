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
        self.spaceHalten = False