import pygame
import sys
import sounds
from screen import screen
from time import time
from hindernise import feld
from startBild import start
from KlasseHeld import Held
from Level1 import Level1
from Level2 import Level2
from Level3 import Level3
from GameOver import gameOver
import DatenSammeln as ds                               # Für den Matlab Beleg


#Das Hauptprgramm
#hier wird der Held erstellt
#Hauptschleife greift auf alle Level zu

zeitmax = 0                                                             #performance test

zeit_start_ges = 0

spieler1 = Held(582, 476, 3, feld, feld, 1, "Held")                    #Figuren erstellen

level = 0                                                                #Startbildschrim

sounds.soundLevel()

go = True

while go:                                                                   #Hauptschleife
    zeit = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0, 0, 0))

    if level == 0:                                                          #Startbildschrim
        level = start()
        zeit_start_ges =time()                                              #Zeit des Startes vom Spiel (für Matlab)

    elif level == 1:                                                         #Geist
        level = Level1(spieler1)

    elif level == 2:                                                         #Harpyie
        level = Level2(spieler1)

    elif level == 3:                                                         #Boss
        level = Level3(spieler1)

    elif level == 4:                                                         #Game Over
        ds.daten_csv(8, round(time() - zeit_start_ges))                      #Gesamt Spielzeit (für Matlab)
        level = gameOver(spieler1)
        spieler1.neu_Position(582, 476, 1)                                   #Held wird resetet für neues Spiel

    pygame.display.update()

    if zeitmax < time() -zeit:                                              #performance Test
        zeitmax = time() -zeit
        #print(zeitmax)