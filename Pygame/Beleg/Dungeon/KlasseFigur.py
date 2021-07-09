import pygame
from screen import screen
from hindernise import grenzeLevel

#Klasse Figur ist die Oberklasse
#Figuren können laufen
#Figuren könne nicht durch Hindernisse laufen

class Figur:
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.level = level                      #In welchem Level befindet sich die Figur (wichtg für die Hindernisse)
        self.kugeln = []
        self.rechteck = pygame.Rect(self.x, self.y, self.breite, self.hoehe)                                    #Welchen Raum nimmt die Figur ein
        self.obenKollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y, 4, 4)                            #diese Rechtecke fungieren als Sensor
        self.untenKollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y + self.hoehe - 4, 4, 4)
        self.rechtsKollision = pygame.Rect(self.x + self.breite - 2, self.y + self.hoehe / 2 - 2, 4, 4)
        self.linksKollision = pygame.Rect(self.x, self.y + self.hoehe / 2 - 2, 4, 4)
        self.schritt = True                                                                                     #Es gibt nur zwei Bilder für Laufen, deswegen Bollien (True, False)
        self.schritteZaehler = 0
        self.schussZaehler = 0
        self.bildFigur = bildFigur
        self.bildOben = [pygame.image.load(f"Bilder/{bildFigur}/Hinten1.png"),
                         pygame.image.load(f"Bilder/{bildFigur}/Hinten2.png")]
        self.bildUnten = [pygame.image.load(f"Bilder/{bildFigur}/Vorn1.png"),
                         pygame.image.load(f"Bilder/{bildFigur}/Vorn2.png")]
        self.bildRechts = [pygame.image.load(f"Bilder/{bildFigur}/Rechts1.png"),
                          pygame.image.load(f"Bilder/{bildFigur}/Rechts2.png")]
        self.bildLinks = [pygame.image.load(f"Bilder/{bildFigur}/Links1.png"),
                           pygame.image.load(f"Bilder/{bildFigur}/links2.png")]


    def laufen(self, richtung):
        self.schritteZaehler += 1
        if self.schritteZaehler % 15 == 0:                                              #Alle 15 Schritte Bild wechseln
            self.schritt = not self.schritt

        if richtung == 0:
            if self.hindernis(self.obenKollision):                                      #wenn kein Hindernis im Weg ist
                self.y -= self.geschw
            screen.blit(self.bildOben[self.schritt], (self.x, self.y))

        elif richtung == 1:
            if self.hindernis(self.untenKollision):
                self.y += self.geschw
            screen.blit(self.bildUnten[self.schritt], (self.x, self.y))

        elif richtung == 2:
            if self.hindernis(self.rechtsKollision):
                self.x += self.geschw
            screen.blit(self.bildRechts[self.schritt], (self.x, self.y))

        elif richtung == 3:
            if self.hindernis(self.linksKollision):
                self.x -= self.geschw
            screen.blit(self.bildLinks[self.schritt], (self.x, self.y))

        self.rechteck = pygame.Rect(self.x, self.y, self.breite, self.hoehe)                            #Aktualisierung der Rechtecke
        self.obenKollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y, 4, 4)
        self.untenKollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y + self.hoehe - 4, 4, 4)
        self.rechtsKollision = pygame.Rect(self.x + self.breite - 2, self.y + self.hoehe / 2 - 2, 4, 4)
        self.linksKollision = pygame.Rect(self.x, self.y + self.hoehe / 2 - 2, 4, 4)


    def hindernis(self, richtung):                                                                      #Hindernisse für die Figur werden überprüft
        r = True
        for i in grenzeLevel[self.level-1]:
            if richtung.colliderect(i):
                r = False
        return r