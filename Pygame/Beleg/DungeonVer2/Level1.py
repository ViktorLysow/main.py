import pygame
import sounds
from screen import screen
from hindernise import feld
from time import time
from KlasseGeist import Geist

hintergrundLevel1 = pygame.image.load("Bilder\Karte\Level1.png")
tor = pygame.Rect(3*feld + feld/2, feld, 5, 5)                                      #Ziel in Level 1

monster = Geist(100, 100, 3, feld, feld, 1, "Geist", time())


def Level1(spieler):
    screen.blit(hintergrundLevel1, (0, 0))
    spieler.steuerung()

    if monster.mLaufen(spieler):
        pygame.display.update()
        pygame.time.wait(1000)
        gameOver = 4
        resetMonsterLevel1()
        return gameOver

    if spieler.obenKollision.colliderect(tor):                        #Held muss mit dem Kopf den eingang berühren
        spieler.x = 582                                                  #Neue position
        spieler.y = 476
        pygame.mixer.Sound.play(sounds.soundTor())
        #pygame.time.wait(500)                                          # überspringt Level 2 ????
        level = 2
        spieler.level = level
        resetMonsterLevel1()
        return level
    else:
        level = 1
        return level

def resetMonsterLevel1():
    monster.dupliList = []
    monster.x = 100
    monster.y =100


