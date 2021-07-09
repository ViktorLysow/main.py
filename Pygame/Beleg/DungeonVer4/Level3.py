import pygame
import sounds
from screen import screen
from hindernise import feld
from time import time
from KlasseBoss import Boss
from KlassePrinzessin_neu import Prinzessin



hintergrundLevel3 = pygame.image.load("Bilder\Karte\Level3.png")
tor = pygame.Rect(7*feld + feld/2, feld, 5, 5)                              #Ziel in Level 3


endBoss = Boss(384,200,3,feld,feld,3,"Boss",time())

prinzessin = Prinzessin(48,48,5,feld,feld,3,"Geist",time())


def Level3(spieler):
    screen.blit(hintergrundLevel3, (0, 0))
    spieler.steuerung()

    if endBoss.mlaufen(spieler) or prinzessin.mlaufen(spieler):
        pygame.display.update()
        pygame.time.wait(1000)
        endBoss.reset()
        gameOver = 4
        return gameOver


    if spieler.obenKollision.colliderect(tor):
        spieler.x = 582
        spieler.y = 476
        pygame.mixer.Sound.play(sounds.soundTor())
        pygame.time.wait(500)
        endBoss.reset()
        gameOver = 4
        return gameOver
    else:
        level = 3
        return level