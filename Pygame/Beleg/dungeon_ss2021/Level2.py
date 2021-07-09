# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Level2
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Organisation und Steuerung des zweiten Levels

from KlasseLevelmanagement import LevelManagement
import pygame
import sounds
from screen import screen
from hindernisse import feld
from time import time
from KlasseBoss import Boss
from KlassePrinzessin import Prinzessin
import DatenSammeln as ds                                                          # Für den Matlab Beleg

zeitStart = True
zeit = 0

hintergrundLevel = pygame.image.load("Bilder\Karte\Level3.png")                    #eigentlich ist unser Level 2 das dritte Level - aber das ist fürs nächste Jahr ;)
tor = pygame.Rect(7*feld + feld/2, feld, 5, 5)                                     #Ziel in Level 3
LevelManagement.Level = 2
endBoss = Boss(48,48,5,feld,feld,LevelManagement.Level,"Boss", time()) # hier den korrekten Aufruf ergänzen (zusätzliche Parameter in Klammern)
prinzessin = Prinzessin(48,48,5,feld,feld,LevelManagement.Level,"Prinzessin", time())


def Level2(spieler):
    global zeitStart, zeit
    screen.blit(hintergrundLevel, (0, 0))

    if zeitStart:                                                                 #Zeit wird ab den ersten aufruf gemäßen (für Matlab)
        zeitStart = False
        LevelManagement.Level = 2
        zeit = time()

    """
    if endBoss.mlaufen(spieler) or prinzessin.mlaufen(spieler, endBoss):          #mit mlaufen läuft der Boss und es wird überprüft ob der Held getötet wurde
        pygame.display.update()                                                   #mit mlaufen läuft die Prinzessin und es wird überprüft ob die Prinzessin getötet wurde
        pygame.time.wait(1000)
        endBoss.reset()                                                           #Es wird Alles für den Boss zurück gesetzt
        prinzessin.reset()                                                        #Es wird Alles für die Prinzessin zurück gesetzt
        LevelManagement.Level = 3
        ds.daten_csv(7, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        ds.daten_csv(9, 3)
        zeitStart = True
        return LevelManagement.Level
    """

    # den folgenden Code-Block (if-Anweisung) können Sie entfernen, wenn Boss implementiert ist. 
    # Dafür dann den Block darüber wieder aktivieren.
    if endBoss.mlaufen(spieler) or prinzessin.mlaufen(spieler, endBoss):             #mit mlaufen läuft die Prinzessin und es wird überprüft ob die Prinzessin getötet wurde
        pygame.display.update()                                                   
        pygame.time.wait(1000)
        endBoss.reset()
        prinzessin.reset()                                                        #Es wird Alles für die Prinzessin zurück gesetzt
        LevelManagement.Level = 3
        ds.daten_csv(9, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        ds.daten_csv(11, 2)
        zeitStart = True
        return LevelManagement.Level

    if spieler.obenKollision.colliderect(tor):                                    #Held muss mit dem Kopf den Eingang berühren
        sounds.soundTor()
        pygame.time.wait(500)
        endBoss.reset()                                                           #Es wird Alles für den Boss zurück gesetzt
        prinzessin.reset()                                                        #Es wird Alles für die Prinzessin zurück gesetzt
        LevelManagement.Level = 3
        ds.daten_csv(9, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        zeitStart = True
        return LevelManagement.Level
    else:                                                                         #Das Level läuft weiter
        spieler.steuerung()        
        return LevelManagement.Level