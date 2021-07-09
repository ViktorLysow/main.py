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


zeitmax = 0                                                             #performance test

spieler1 = Held(582,476,3,feld,feld,1,"Held")                            #Figuren erstellen

level = 0                                                                #Startbildschrim

sounds.soundLevel()

go = True

while go:                                                                   #Hauptschleife
    zeit = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0,0,0))

    if level == 0:                                                          #Startbildschrim
        level = start()

    elif level == 1:                                                         #Geist
        level = Level1(spieler1)

    elif level == 2:                                                         #Harpyie
        level = Level2(spieler1)

    elif level == 3:                                                         #Boss
        level = Level3(spieler1)

    elif level == 4:                                                         #Game Over
        level = gameOver()
        spieler1 = Held(582, 476, 3, feld, feld, 3, "Held")

    pygame.display.update()

    if zeitmax < time() -zeit:                     #performance test
        zeitmax = time() -zeit
        #print(zeitmax)