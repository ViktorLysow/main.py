# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Hauptprogramm
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Steuerung des gesamten Spielablaufs - dieses Programm muss gestartet werden, um das Spiel zu spielen.
#
# Das Hauptprgramm
# hier wird der Held erstellt
# Hauptschleife greift auf alle Level zu

from KlasseLevelmanagement import LevelManagement
import pygame
import sys
import sounds
from screen import screen
from time import time
from hindernisse import feld
from startBild import start
from KlasseHeld import Held
from Level1 import Level1
from Level2 import Level2
from GameOver import gameOver
import DatenSammeln as ds                               # Für den Matlab Beleg



zeitmax = 0                                                             #performance test
zeit_start_ges = 0

spieler1 = Held(582, 476, 3, feld, feld, 1, "Held")                    #Figuren erstellen
sounds.soundLevel()
LevelManagement.Level = 0

go = True

while go:                                                                   #Hauptschleife
    zeit = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0, 0, 0))

    if LevelManagement.Level == 0:                                                          #Startbildschrim
        LevelManagement.Level = start()
        zeit_start_ges =time()                                              #Zeit des Startes vom Spiel (für Matlab)

    elif LevelManagement.Level == 1:                                                         #Geist
        LevelManagement.Level = Level1(spieler1)

    elif LevelManagement.Level == 2:                                                         #Boss
        LevelManagement.Level = Level2(spieler1)

    elif LevelManagement.Level == 3:                                                         #Game Over
        ds.daten_csv(8, round(time() - zeit_start_ges))                      #Gesamt Spielzeit (für Matlab)
        LevelManagement.Level = gameOver(spieler1)
        spieler1.neu_Position(582, 476, 1)                                   #Held wird resetet für neues Spiel

    pygame.display.update()

    if zeitmax < time() - zeit:                                              #performance Test
        zeitmax = time() - zeit
        #print(zeitmax)