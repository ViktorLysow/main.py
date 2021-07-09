import pygame
import sys
import time
import random

pygame.init()
hintergrundLevel1 = pygame.image.load("Bilder\Karte\Level1.png")
hintergrundLevel2 = pygame.image.load("Bilder\Karte\Level2.png")
hintergrundLevel3 = pygame.image.load("Bilder\Karte\Level3.png")

hintergrundstart1 = pygame.image.load("Bilder\Start\Start1.png")
hintergrundstart2 = pygame.image.load("Bilder\Start\Medieval.jpg")

levelSound = pygame.mixer.Sound("Sound/level.wav")
levelSound.set_volume(0.5)
levelBossSound = pygame.mixer.Sound("Sound/levelBoss.wav")
levelBossSound.set_volume(0.5)

screen = pygame.display.set_mode([816,624])
clock = pygame.time.Clock()
pygame.display.set_caption("Spiel")
font = pygame.font.SysFont('Impact', 20)

feld = 48 # pixel

grenzeLevel1 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*5, feld, feld*2, feld*4),0),
               pygame.draw.rect(screen, (0,0,0), (feld*3, feld*2,feld*2, feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*7, feld*6,feld*2, feld*6),0),
               pygame.draw.rect(screen, (0,0,0), (feld*9, feld*6,feld*4, feld),0)]

grenzeLevel2 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0),
                pygame.draw.rect(screen, (0,0,0), (feld,feld,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*8,feld*3,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*5,feld*6,feld*2,feld*4),0),
                pygame.draw.rect(screen, (0,0,0), (feld*3,feld*7,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*10,feld*7,feld*2,feld*3),0),
                pygame.draw.rect(screen, (0,0,0), (feld*9,feld*8,feld,feld),0)]

grenzeLevel3 =[pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0)]

grenzeLevel= []
grenzeLevel.append(grenzeLevel1)
grenzeLevel.append(grenzeLevel2)
grenzeLevel.append(grenzeLevel3)

tor1 = pygame.Rect(3*feld+ feld/2, feld, 5, 5)
tor2 = pygame.Rect(7*feld + feld/2, feld, 5, 5)

class Figur:
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.rechteck = pygame.Rect(self.x, self.y, self.breite, self.hoehe)
        self.obenkollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y, 4, 4)
        self.untenkollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y + self.hoehe - 4, 4, 4)
        self.rechtskollision = pygame.Rect(self.x + self.breite - 2, self.y + self.hoehe / 2 - 2, 4, 4)
        self.linkskollision = pygame.Rect(self.x, self.y + self.hoehe / 2 - 2, 4, 4)
        self.schritt = True
        self.schritteZaehler = 0
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
        if self.schritteZaehler % 15 == 0:
            self.schritt = not self.schritt

        if richtung == 0:
            if self.hindernis(self.obenkollision):
                self.y -= self.geschw
            screen.blit(self.bildOben[self.schritt], (self.x, self.y))
        elif richtung == 1:
            if self.hindernis(self.untenkollision):
                self.y += self.geschw
            screen.blit(self.bildUnten[self.schritt], (self.x, self.y))
        elif richtung == 2:
            if self.hindernis(self.rechtskollision):
                self.x += self.geschw
            screen.blit(self.bildRechts[self.schritt], (self.x, self.y))
        elif richtung == 3:
            if self.hindernis(self.linkskollision):
                self.x -= self.geschw
            screen.blit(self.bildLinks[self.schritt], (self.x, self.y))

        self.rechteck = pygame.Rect(self.x, self.y, self.breite, self.hoehe)
        self.obenkollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y, 4, 4)
        self.untenkollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y + self.hoehe - 4, 4, 4)
        self.rechtskollision = pygame.Rect(self.x + self.breite - 2, self.y + self.hoehe / 2 - 2, 4, 4)
        self.linkskollision = pygame.Rect(self.x, self.y + self.hoehe / 2 - 2, 4, 4)





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

    def hindernis(self,richtung):
        r = True
        for i in grenzeLevel[level-1]:
            if richtung.colliderect(i):
                r = False
        return r

class Monster(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur)
        self.richtung = 1
        self.zeitMonster = zeitMonster

    def mLaufen(self):
        if time.time() - self.zeitMonster >= 1:
            self.richtung = random.randint(0, 3)
            self.zeitMonster = time.time()
        self.laufen(self.richtung)


class Geist (Monster):
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur,zeitMonster)

    def hindernis(self,richtung):
        r = True
        for i in grenzeLevel[level-1]:
            if richtung.colliderect(i):
                r = False
        return r



class Harpyie (Monster):
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur,zeitMonster)
    def hindernis(self,richtung):
        r = True
        for i in grenzeLevel[2]:
            if richtung.colliderect(i):
                r = False
        return r



class Boss (Geist, Harpyie):
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur,zeitMonster)

    def hindernis(self,richtung):
        r = True
        for i in grenzeLevel[level-1]:
            if richtung.colliderect(i):
                r = False
        return r




def steurung():
    global stehRicht
    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_UP]:
        spieler1.laufen(0)
        stehRicht = 0
    elif gedrueckt[pygame.K_DOWN]:
        spieler1.laufen(1)
        stehRicht = 1
    elif gedrueckt[pygame.K_RIGHT]:
        spieler1.laufen(2)
        stehRicht = 2
    elif gedrueckt[pygame.K_LEFT]:
        spieler1.laufen(3)
        stehRicht = 3
    else:
        spieler1.stehen(stehRicht)



aktivButton = False

def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(bx, by, nachricht, laenge, hoehe, farbe_normal, farbe_aktiv, randDicke, maus, klick):
    global aktivButton
    if maus[0] > bx and maus[0] < bx + laenge and maus[1] > by and maus[1] < by + hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx, by, laenge, hoehe))
        if klick[0] == 1 and aktivButton == False:
            aktivButton = True
            if nachricht == "Neues Spiel":
                return True
            elif nachricht == "Ende":
                sys.exit()
        if klick[0] == 0:
            aktivButton = False
    else:
        pygame.draw.rect(screen, farbe_normal, (bx, by, laenge, hoehe))
    pygame.draw.rect(screen, (0, 0, 0), (bx, by, laenge, hoehe), randDicke)
    textGrund, textKasten = textObjekt(nachricht, font)
    textKasten.center = ((bx + (laenge / 2)), (by + (hoehe / 2)))
    screen.blit(textGrund, textKasten)
    return False


def start():
    screen.blit(hintergrundstart1, (0, 0))
    pygame.mixer.Sound.stop(levelBossSound)
    pygame.mixer.Sound.play(levelSound)

    maus = pygame.mouse.get_pos()
    klick = pygame.mouse.get_pressed()
    neuesSpeiel =button(348, 250, "Neues Spiel", 120, 60, (0, 150, 0), (0, 255, 0), 1, maus, klick)
    button(348, 400, "Ende", 120, 60, (150, 0, 0), (255, 0, 0), 1, maus,klick)

    pygame.display.update()
    if neuesSpeiel:
        del maus
        del klick
    return neuesSpeiel

def Level1():
    screen.blit(hintergrundLevel1, (0, 0))
    steurung()
    monster1.mLaufen()

    if spieler1.obenkollision.colliderect(tor1):
        spieler1.x = 582
        spieler1.y = 476
        pygame.mixer.Sound.play(levelSound)
        return True
    else:
        return False

def Level2():
    screen.blit(hintergrundLevel2, (0, 0))
    steurung()
    monster2.mLaufen()

    if spieler1.obenkollision.colliderect(tor1):
        spieler1.x = 582
        spieler1.y = 476
        pygame.mixer.Sound.stop(levelSound)
        pygame.mixer.Sound.play(levelBossSound)
        return True
    else:
        return False

def Level3():
    screen.blit(hintergrundLevel3, (0, 0))
    steurung()
    monster3.mLaufen()

    if spieler1.obenkollision.colliderect(tor2):
        spieler1.x = 582
        spieler1.y = 476
        return True
    else:
        return False

zeitmax = 0
zeitstart = time.time()

stehRicht = 0
spieler1 = Held(582,476,3,feld,feld,"Held")

monster1 = Geist(100,100,3,feld,feld,"Geist",time.time())
monster2 = Harpyie(100,100,3,feld,feld,"Harpyie",time.time())
monster3 = Boss(100,100,3,feld,feld,"Boss",time.time())
level = 0

go = True



while go:
    zeit = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0,0,0))

    if level == 0:
        level += start()

    if level == 1:
        level += Level1()

    if level == 2:
        level += Level2()

    if level == 3:
        level += Level3()

    if level == 4:
        screen.blit(pygame.image.load("Bilder\GameOver.png"), (0, 0))
        pygame.display.update()
        pygame.time.wait(2000)
        level = 0

    pygame.display.update()

    if zeitmax < time.time() -zeit:
        zeitmax = time.time() -zeit
        #print(zeitmax)