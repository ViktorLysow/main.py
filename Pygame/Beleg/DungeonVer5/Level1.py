import pygame
import sounds
from screen import screen
from hindernise import feld
from time import time
from KlasseGeist import Geist
from KlasseFalle import Falle


hintergrundLevel1 = pygame.image.load("Bilder\Karte\Level1.png")
tor = pygame.Rect(3*feld + feld/2, feld, 5, 5)                                      #Ziel in Level 1

monster = Geist(100, 100, 3, feld, feld, 1, "Geist", time())
falle = Falle(2 * feld, 2 * feld)

def Level1(spieler):
    screen.blit(hintergrundLevel1, (0, 0))


    if falle.bewegung(spieler) or monster.mlaufen(spieler):           #mit mlaufen läuft der Geist und es wird überprüft, ob der Held getötet wurde
        pygame.display.update()
        pygame.time.wait(1000)
        gameOver = 4
        monster.reset()                                               #Es wird Alles für den Geist zurück gesetzt
        return gameOver

    if spieler.obenKollision.colliderect(tor):                        #Held muss mit dem Kopf den Eingang berühren
        level = 2
        spieler.neu_Position(582, 476, level)                         #Neue Position für das nächste Level
        sounds.soundTor()
        pygame.time.wait(500)
        monster.reset()                                                #Es wird Alles für den Geist zurück gesetzt
        return level
    else:                                                              #Das Level läuft weiter
        spieler.steuerung()
        level = 1
        return level



