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


screen = pygame.display.set_mode([816, 624])
clock = pygame.time.Clock()
pygame.display.set_caption("Dungen")
font = pygame.font.SysFont('Impact', 20)

soundtor = pygame.mixer.Sound("Sound/tor.wav")
soundtor.set_volume(0.5)

feld = 48 # pixel

grenzeLevel1 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),             # kollisionen in Level1
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*5, feld, feld*2, feld*4),0),
               pygame.draw.rect(screen, (0,0,0), (feld*3, feld*2,feld*2, feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*7, feld*6,feld*2, feld*6),0),
               pygame.draw.rect(screen, (0,0,0), (feld*9, feld*6,feld*4, feld),0)]

grenzeLevel2 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),               # kollisionen in Level2
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

grenzeLevel3 =[pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),                 # kollisionen in Level2
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0)]

grenzeLevel= []                                                                         #liste mit allen Hindernisen
grenzeLevel.append(grenzeLevel1)
grenzeLevel.append(grenzeLevel2)
grenzeLevel.append(grenzeLevel3)

tor1 = pygame.Rect(3*feld+ feld/2, feld, 5, 5)                                          #Zeiel ist es zum Tor zu kommen
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
        if self.schritteZaehler % 15 == 0:                                              #Alle 15 schritte Bild wechseln
            self.schritt = not self.schritt

        if richtung == 0:
            if self.hindernis(self.obenkollision):                                      #wenn kein Hindernis im weg ist
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

        self.rechteck = pygame.Rect(self.x, self.y, self.breite, self.hoehe)                            #aktualisierung der Rechtecke
        self.obenkollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y, 4, 4)
        self.untenkollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y + self.hoehe - 4, 4, 4)
        self.rechtskollision = pygame.Rect(self.x + self.breite - 2, self.y + self.hoehe / 2 - 2, 4, 4)
        self.linkskollision = pygame.Rect(self.x, self.y + self.hoehe / 2 - 2, 4, 4)

    def hindernis(self, richtung):                                                                      #hindernise für die Figur werden überprüft
        r = True
        for i in grenzeLevel[level-1]:
            if richtung.colliderect(i):
                r = False
        return r



class Held(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur)
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
            spieler1.laufen(0)
            self.stehRicht = 0
        elif self.gedrueckt[pygame.K_DOWN]:
            spieler1.laufen(1)
            self.stehRicht = 1
        elif self.gedrueckt[pygame.K_RIGHT]:
            spieler1.laufen(2)
            self.stehRicht = 2
        elif self.gedrueckt[pygame.K_LEFT]:
            spieler1.laufen(3)
            self.stehRicht = 3
        else:
            self.stehen()




class Monster(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur)
        self.richtung = 1
        self.zeitMonster = zeitMonster

    def mLaufen(self):                                                              #Monster können selber laufen
        if time.time() - self.zeitMonster >= 1:                                     #abhängig von der zeit
            self.richtung = random.randint(0, 3)
            self.zeitMonster = time.time()
        self.laufen(self.richtung)




class Geist (Monster):                                                              #Geist soll sich noch duplizieren
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur,zeitMonster)


    #def duplizieren(self):





class Harpyie (Monster):                                                            #Harpyie soll in allen 4 Richtungen hin und wieder schißen
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur, zeitMonster)

    def hindernis(self,richtung):                                                   #kann über Lava fliegen
        r = True
        for i in grenzeLevel[2]:
            if richtung.colliderect(i):
                r = False
        return r



class Boss (Geist, Harpyie):                                                        #Boss soll alle Monster fähigkeiten haben + vielleicht noch eine
    def __init__(self, x, y, geschw, breite, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, bildFigur,zeitMonster)




aktivButton = False

def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(bx, by, nachricht, laenge, hoehe, farbe_normal, farbe_aktiv, randDicke, maus, klick):    # irgendwo aus dem internet :)
    global aktivButton
    if maus[0] > bx and maus[0] < bx + laenge and maus[1] > by and maus[1] < by + hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx, by, laenge, hoehe))
        if klick[0] == 1 and aktivButton == False:
            aktivButton = True
            if nachricht == "Neues Spiel":
                pygame.mixer.Sound.play(soundtor)
                pygame.time.wait(1000)
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




def start():                                                                    #Startbildschrim
    screen.blit(hintergrundstart1, (0, 0))
    maus = pygame.mouse.get_pos()
    klick = pygame.mouse.get_pressed()
    neuesSpeiel =button(348, 250, "Neues Spiel", 120, 60, (0, 150, 0), (0, 255, 0), 1, maus, klick)
    button(348, 400, "Ende", 120, 60, (150, 0, 0), (255, 0, 0), 1, maus,klick)

    if neuesSpeiel:
        del maus
        del klick
    return neuesSpeiel

def Level1():
    screen.blit(hintergrundLevel1, (0, 0))
    spieler1.steurung()
    monster1.mLaufen()

    if spieler1.sterben(monster1.rechteck):                                #!!! versuche grade das Sterben einzuführen !!!
        pygame.display.update()
        pygame.time.wait(1000)
        gameOver = 4
        return gameOver

    if spieler1.obenkollision.colliderect(tor1):                        #Held muss mit dem Kopf den eingang berühren
        spieler1.x = 582                                                  #Neue position
        spieler1.x = 582
        spieler1.y = 476
        pygame.mixer.Sound.play(soundtor)
        #pygame.time.wait(500)                      # überspringt Level 2 ????
        level = 2
        return level
    else:
        level = 1
        return level


def Level2():
    screen.blit(hintergrundLevel2, (0, 0))
    spieler1.steurung()
    monster2.mLaufen()
    monster3.mLaufen()

    if spieler1.obenkollision.colliderect(tor1):
        spieler1.x = 582
        spieler1.y = 476
        pygame.mixer.Sound.play(soundtor)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Sound/levelBoss.mp3")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.6)
        pygame.time.wait(500)
        level = 3
        return level
    else:
        level = 2
        return level

def Level3():
    screen.blit(hintergrundLevel3, (0, 0))
    spieler1.steurung()
    endBoss.mLaufen()

    if spieler1.obenkollision.colliderect(tor2):
        spieler1.x = 582
        spieler1.y = 476
        pygame.mixer.Sound.play(soundtor)
        pygame.time.wait(500)
        gameOver = 4
        return gameOver
    else:
        level = 3
        return level

zeitmax = 0                                                             #performance test


spieler1 = Held(582,476,3,feld,feld,"Held")                             # Fieguren erstellen

monster1 = Geist(100,100,3,feld,feld,"Geist",time.time())

monster2 = Harpyie(200,150,3,feld,feld,"Harpyie",time.time())
monster3 = Harpyie(300,200,3,feld,feld,"Harpyie",time.time())

endBoss = Boss(384,200,3,feld,feld,"Boss",time.time())


level = 0                                                                #Startbildschrim

pygame.mixer.music.load("Sound/level.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(1)

go = True

while go:                                                                   #Hauptschleife
    zeit = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0,0,0))

    if level == 0:                                                          #Startbildschrim
        level = start()

    elif level == 1:                                                         #Geist
        level = Level1()

    elif level == 2:                                                         #Harpyie
        level = Level2()

    elif level == 3:                                                         #Boss
        level = Level3()

    elif level == 4:                                                                #Game Over
        screen.blit(pygame.image.load("Bilder\GameOver.png"), (0, 0))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Sound/level.mp3")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(1)
        spieler1 = Held(582, 476, 3, feld, feld, "Held")
        level = 0

    pygame.display.update()

    if zeitmax < time.time() -zeit:                     #performance test
        zeitmax = time.time() -zeit
        #print(zeitmax)