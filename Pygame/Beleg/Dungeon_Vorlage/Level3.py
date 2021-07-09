import pygame
import sounds
from screen import screen
from hindernise import feld
from time import time
from KlasseMonster import Monster



hintergrundLevel3 = pygame.image.load("Bilder\Karte\Level3.png")
tor = pygame.Rect(7*feld + feld/2, feld, 5, 5)                                   #Ziel in Level 3


endBoss = Monster(384,200,3,feld,feld,3,"Drache",time())                        #KlasseBoss !!!


def Level3(spieler):
    screen.blit(hintergrundLevel3, (0, 0))

    if endBoss.mlaufen(spieler):                                                #mit mlaufen läuft der Boss und es wird überprüft ob der Held getötet wurde
        pygame.display.update()
        pygame.time.wait(1000)
        endBoss.reset()                                                           #Es wird Alles für den Boss zurück gesetzt
        gameOver = 4
        return gameOver

    if spieler.obenKollision.colliderect(tor):                                    #Held muss mit dem Kopf den Eingang berühren
        sounds.soundTor()
        pygame.time.wait(500)
        endBoss.reset()                                                           #Es wird Alles für den Boss zurück gesetzt
        gameOver = 4
        return gameOver
    else:                                                                         #Das Level läuft weiter
        spieler.steuerung()
        level = 3
        return level