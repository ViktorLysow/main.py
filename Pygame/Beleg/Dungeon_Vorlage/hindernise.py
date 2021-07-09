import pygame
from screen import screen

feld = 48 # pixel

grenzeLevel1 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),                 # Kollisionen in Level1
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0)]

grenzeLevel2 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),                 # Kollisionen in Level2
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0)]

grenzeLevel3 =[pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),                 # Kollisionen in Level3
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0)]

grenzeLevel= []                                                                         #liste mit allen Hindernissen
grenzeLevel.append(grenzeLevel1)
grenzeLevel.append(grenzeLevel2)
grenzeLevel.append(grenzeLevel3)