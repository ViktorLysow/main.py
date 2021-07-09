# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Level1
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Organisation und Steuerung des ersten Levels

from KlasseLevelmanagement import LevelManagement
import pygame
import sounds
import DatenSammeln as ds                           # Für den Matlab Beleg
from screen import screen
from hindernisse import feld
from time import time
from KlasseGeist import Geist

zeitStart = True
zeit = 0

LevelManagement.Level = 1
hintergrundLevel1 = pygame.image.load("Bilder\Karte\Level1.png")
tor = pygame.Rect(3*feld + feld/2, feld, 5, 5)                                      #Ziel in Level 1

monster = Geist(100, 100, 3, feld, feld, LevelManagement.Level, "Geist", time())

def Level1(spieler):
    global zeitStart, zeit
    screen.blit(hintergrundLevel1, (0, 0))

    if zeitStart:                                                     #Zeit wird ab den ersten aufruf gemäßen (für Matlab)
        zeitStart = False
        LevelManagement.Level = 1
        zeit = time()

    if monster.mlaufen(spieler):           #mit mlaufen läuft der Geist und es wird überprüft, ob der Held getötet wurde
        pygame.display.update()
        pygame.time.wait(1000)
        gameOver = 3
        monster.reset()                                               #Es wird Alles für den Geist zurück gesetzt
        ds.daten_csv(8,round(time() - zeit))                          #Zeit für Level1 (für Matlab)
        ds.daten_csv(11,1)
        zeitStart = True
        return gameOver

    if spieler.obenKollision.colliderect(tor):                        #Held muss mit dem Kopf den Eingang berühren
        LevelManagement.Level += 1
        spieler.neu_Position(582, 476, LevelManagement.Level)                         #Neue Position für das nächste Level
        sounds.soundTor()
        pygame.time.wait(500)
        monster.reset()                                                #Es wird Alles für den Geist zurück gesetzt
        ds.daten_csv(8, round(time() - zeit))                          #Zeit für Level1 (für Matlab)
        zeitStart = True
        return LevelManagement.Level 
    else:                                                              #Das Level läuft weiter
        spieler.steuerung()
        return LevelManagement.Level



