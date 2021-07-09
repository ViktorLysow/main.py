import pygame
import sounds
from screen import screen
from hindernise import feld
from time import time
from KlasseBoss import Boss
import KlasseGeist


hintergrundLevel3 = pygame.image.load("Bilder\Karte\Level3.png")
tor = pygame.Rect(7*feld + feld/2, feld, 5, 5)                              #Ziel in Level 3

KlasseGeist.anzahl = 1

endBoss = Boss(384,200,3,feld,feld,3,"Boss",time())


def Level3(spieler):
    screen.blit(hintergrundLevel3, (0, 0))
    spieler.steuerung()
    endBoss.mLaufen()

    if spieler.obenKollision.colliderect(tor):
        spieler.x = 582
        spieler.y = 476
        pygame.mixer.Sound.play(sounds.soundTor())
        pygame.time.wait(500)
        gameOver = 4
        return gameOver
    else:
        level = 3
        return level