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
    spieler.steuerung()

    if monster1.mlaufen(spieler) or monster2.mlaufen(spieler):                                #!!! versuche grade das Sterben einzuführen !!!
        pygame.display.update()
        pygame.time.wait(1000)
        monster1.reset()
        monster2.reset()
        gameOver = 4
        return gameOver

    if spieler.obenKollision.colliderect(tor):
        spieler.x = 582
        spieler.y = 476
        pygame.mixer.Sound.play(sounds.soundTor())
        sounds.soundBoss()
        pygame.time.wait(500)
        monster1.reset()
        monster2.reset()
        level = 3
        spieler.level = 3
        return level
    else:
        level = 2
        return level