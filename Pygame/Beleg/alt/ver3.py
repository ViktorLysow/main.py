import pygame
import sys

pygame.init()
hintergrundLevel1 = pygame.image.load("Bilder\Karte\Level1.png")
screen = pygame.display.set_mode([816,624])
clock = pygame.time.Clock()
pygame.display.set_caption("ver1")

x = 300
y = 300

geschw = 3
breite = 48
hoehe = 48

linkeWand = pygame.draw.rect(screen, (0,0,0), (0,0,48,624),0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (816,0,-48,624),0)
obenWand = pygame.draw.rect(screen, (0,0,0), (0,0,816,48),0)
untenWand = pygame.draw.rect(screen,(0,0,0),(0,624,816,-48),0)


class Figur:
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.schritt = True
        self.schritteZähler = 0
        self.bildOben = [pygame.image.load(f"Bilder/{bildFigur}/Hinten1.png"),
                         pygame.image.load(f"Bilder/{bildFigur}/Hinten2.png")]
        self.bildUnten = [pygame.image.load(f"Bilder/{bildFigur}/Vorn1.png"),
                         pygame.image.load(f"Bilder/{bildFigur}/Vorn2.png")]
        self.bildRechts = [pygame.image.load(f"Bilder/{bildFigur}/Rechts1.png"),
                          pygame.image.load(f"Bilder/{bildFigur}/Rechts2.png")]
        self.bildLinks = [pygame.image.load(f"Bilder/{bildFigur}/Links1.png"),
                           pygame.image.load(f"Bilder/{bildFigur}/links2.png")]

    def laufen(self, richtung):
        self.schritteZähler += 1
        if self.schritteZähler % 15 == 0:
            self.schritt = not self.schritt

        if richtung == 0:
            self.y -= self.geschw
            screen.blit(self.bildOben[self.schritt], (self.x, self.y))
        elif richtung == 1:
            self.y += self.geschw
            screen.blit(self.bildUnten[self.schritt], (self.x, self.y))
        elif richtung == 2:
            self.x += self.geschw
            screen.blit(self.bildRechts[self.schritt], (self.x, self.y))
        elif richtung == 3:
            self.x -= self.geschw
            screen.blit(self.bildLinks[self.schritt], (self.x, self.y))



class Held(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur)
        self.bildOben.append(pygame.image.load(f"Bilder/{bildFigur}/HintenS.png"))
        self.bildUnten.append(pygame.image.load(f"Bilder/{bildFigur}/VornS.png"))
        self.bildRechts.append(pygame.image.load(f"Bilder/{bildFigur}/RechtsS.png"))
        self.bildLinks.append(pygame.image.load(f"Bilder/{bildFigur}/LinksS.png"))

    def stehen(self,richtung):
        if richtung == 0:
            screen.blit(self.bildOben[2], (self.x, self.y))
        if richtung == 1:
            screen.blit(self.bildUnten[2], (self.x, self.y))
        if richtung == 2:
            screen.blit(self.bildRechts[2], (self.x, self.y))
        if richtung == 3:
            screen.blit(self.bildLinks[2], (self.x, self.y))



go = True

stehRicht = 0

spieler1 = Held(582,528,3,48,48,"Held")


def steurung():
    global stehRicht
    spielerRechteck = pygame.Rect(spieler1.x, spieler1.y, 48, 48)
    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_UP] and not spielerRechteck.colliderect(obenWand):
        spieler1.laufen(0)
        stehRicht = 0
    elif gedrueckt[pygame.K_DOWN] and not spielerRechteck.colliderect(untenWand):
        spieler1.laufen(1)
        stehRicht = 1
    elif gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        spieler1.laufen(2)
        stehRicht = 2
    elif gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        spieler1.laufen(3)
        stehRicht = 3
    else:
        spieler1.stehen(stehRicht)

def Level1():
    screen.blit(hintergrundLevel1, (0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (142, 46, 48, 48))
    SpielerRechteck = pygame.Rect(spieler1.x + 18, spieler1.y + 18, spieler1.breite, spieler1.hoehe)
    tor = pygame.Rect(142, 46, 48, 48)

    if SpielerRechteck.colliderect(tor):
        return True
    else:
        return False

level = 1

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if level == 1:
        level += Level1()

    steurung()

    if level == 2:
        screen.blit(pygame.image.load("Bilder\GameOver.png"), (0, 0))
    pygame.display.update()

    clock.tick(60)