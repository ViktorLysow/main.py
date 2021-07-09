import pygame
import sounds
from screen import screen
from hindernise import feld
from time import time
from KlasseHarpyie import Harpyie

hintergrundLevel2 = pygame.image.load("Bilder\Karte\Level2.png")
tor = pygame.Rect(3*feld+ feld/2, feld, 5, 5)                                      #Ziel in Level 2

monster1 = Harpyie(200,150,3,feld,feld,2,"Harpyie",time())
monster2 = Harpyie(300,200,3,feld,feld,2,"Harpyie",time())

def Level2(spieler):
    screen.blit(hintergrundLevel2, (0, 0))

    if monster1.mlaufen(spieler) or monster2.mlaufen(spieler):                  # mit mlaufen laufen(fliegen) die Harpyien und es wird überprüft ob der Held getötet wurde
        pygame.display.update()
        pygame.time.wait(1000)
        monster1.reset()                                                        #Es wird Alles von den Harpyien zurück gesetzt
        monster2.reset()
        gameOver = 4
        return gameOver

    if spieler.obenKollision.colliderect(tor):                                  #Held muss mit dem Kopf den Eingang berühren
        level = 3
        spieler.neu_Position(582, 476, level)                                   #Neue Position für das nächste Level
        sounds.soundTor()
        sounds.soundBoss()
        pygame.time.wait(500)
        monster1.reset()                                                        #Es wird Alles von den Harpyien zurück gesetzt
        monster2.reset()
        return level
    else:                                                                       #Das Level läuft weiter
        spieler.steuerung()
        level = 2
        return level