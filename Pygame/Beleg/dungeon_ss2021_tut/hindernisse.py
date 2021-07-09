# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Hindernisse
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 28.04.2021
# Zweck: Definition der vorhandenen Hinternisse
 
import pygame
from screen import screen

feld = 48 # pixel

grenzeLevel1 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),             # Kollisionen in Level1
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*5, feld, feld*2, feld*4),0),
               pygame.draw.rect(screen, (0,0,0), (feld*3, feld*2,feld*2, feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*7, feld*6,feld*2, feld*6),0),
               pygame.draw.rect(screen, (0,0,0), (feld*9, feld*6,feld*4, feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*16,0, feld, 13*feld),0),
               pygame.draw.rect(screen, (0,0,0), (0, feld*12, feld*17, feld),0)]


grenzeLevel2 =[pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),                 # Kollisionen in Level2
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0),
               pygame.draw.rect(screen, (0,0,0), (feld*16,0, feld, 13*feld),0),
               pygame.draw.rect(screen, (0,0,0), (0, feld*12, feld*17, feld),0)]

grenzeLevel= []                                                                         #liste mit allen Hindernissen
grenzeLevel.append(grenzeLevel1)
grenzeLevel.append(grenzeLevel2)

tor1 = pygame.Rect(3*feld + feld/2, feld, 5, 5)                                      #Ziel in Level 1 und 2
tor2 = pygame.Rect(7*feld + feld/2, feld, 5, 5)                                     #Ziel in Level 3