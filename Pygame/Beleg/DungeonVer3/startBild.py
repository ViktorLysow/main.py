import pygame
from screen import screen
from button import button

hintergrundstart1 = pygame.image.load("Bilder\Start\Start1.png")

def start():                                                                    #Startbildschrim
    screen.blit(hintergrundstart1, (0, 0))
    maus = pygame.mouse.get_pos()
    klick = pygame.mouse.get_pressed()
    neuesSpeiel =button(348, 250, "Neues Spiel", 120, 60, (0, 150, 0), (0, 255, 0), 1, maus, klick)
    button(348, 400, "Ende", 120, 60, (150, 0, 0), (255, 0, 0), 1, maus,klick)

    if neuesSpeiel:
        del maus
        del klick
    return neuesSpeiel