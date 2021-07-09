import pygame
import sounds
from screen import screen
from hindernise import feld
from time import time
from KlasseBoss import Boss
from KlassePrinzessin import Prinzessin
import DatenSammeln as ds                                                          # Für den Matlab Beleg

zeitStart = True
zeit = 0

hintergrundLevel3 = pygame.image.load("Bilder\Karte\Level3.png")
tor = pygame.Rect(7*feld + feld/2, feld, 5, 5)                                     #Ziel in Level 3


endBoss = Boss(384,200,3,feld,feld,3,"Drache",time())
prinzessin = Prinzessin(48,48,5,feld,feld,3,"Prinzessin", time())


def Level3(spieler):
    global zeitStart, zeit
    screen.blit(hintergrundLevel3, (0, 0))

    if zeitStart:                                                                 #Zeit wird ab den ersten aufruf gemäßen (für Matlab)
        zeitStart = False
        zeit = time()

    if endBoss.mlaufen(spieler) or prinzessin.mlaufen(spieler, endBoss):          #mit mlaufen läuft der Boss und es wird überprüft ob der Held getötet wurde
        pygame.display.update()                                                   #mit mlaufen läuft die Prinzessin und es wird überprüft ob die Prinzessin getötet wurde
        pygame.time.wait(1000)
        endBoss.reset()                                                           #Es wird Alles für den Boss zurück gesetzt
        prinzessin.reset()                                                        #Es wird Alles für die Prinzessin zurück gesetzt
        gameOver = 4
        ds.daten_csv(7, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        ds.daten_csv(9, 3)
        zeitStart = True
        return gameOver


    if spieler.obenKollision.colliderect(tor):                                    #Held muss mit dem Kopf den Eingang berühren
        sounds.soundTor()
        pygame.time.wait(500)
        endBoss.reset()                                                           #Es wird Alles für den Boss zurück gesetzt
        prinzessin.reset()                                                        #Es wird Alles für die Prinzessin zurück gesetzt
        gameOver = 4
        ds.daten_csv(7, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        zeitStart = True
        return gameOver
    else:                                                                         #Das Level läuft weiter
        spieler.steuerung()
        level = 3
        return level