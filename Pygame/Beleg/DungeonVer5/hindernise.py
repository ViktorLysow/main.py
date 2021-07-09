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
               pygame.draw.rect(screen, (0,0,0), (feld*9, feld*6,feld*4, feld),0)]

grenzeLevel2 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),               # Kollisionen in Level2
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0),
                pygame.draw.rect(screen, (0,0,0), (feld,feld,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*8,feld*3,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*5,feld*6,feld*2,feld*4),0),
                pygame.draw.rect(screen, (0,0,0), (feld*3,feld*7,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*10,feld*7,feld*2,feld*3),0),
                pygame.draw.rect(screen, (0,0,0), (feld*9,feld*8,feld,feld),0)]

grenzeLevel3 =[pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*13),0),                 # Kollisionen in Level2
               pygame.draw.rect(screen, (0,0,0), (feld*17,0,-feld,feld*13),0),
               pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0),
               pygame.draw.rect(screen, (0,0,0), (0,feld*13,feld*17,-feld),0)]

grenzeLevel= []                                                                         #liste mit allen Hindernissen
grenzeLevel.append(grenzeLevel1)
grenzeLevel.append(grenzeLevel2)
grenzeLevel.append(grenzeLevel3)

tor1 = pygame.Rect(3*feld + feld/2, feld, 5, 5)                                      #Ziel in Level 1 und 2
tor2 = pygame.Rect(7*feld + feld/2, feld, 5, 5)                                     #Ziel in Level 3