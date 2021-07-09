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
    monster.mLaufen()

    if spieler.sterben(monster.rechteck):                                #!!! versuche grade das Sterben einzuführen !!!
        pygame.display.update()
        pygame.time.wait(1000)
        gameOver = 4
        return gameOver

    if spieler.obenKollision.colliderect(tor):                        #Held muss mit dem Kopf den eingang berühren
        spieler.x = 582                                                  #Neue position
        spieler.x = 582
        spieler.y = 476
        pygame.mixer.Sound.play(sounds.soundTor())
        #pygame.time.wait(500)                                          # überspringt Level 2 ????
        level = 2
        spieler.level = level
        return level
    else:
        level = 1
        return level