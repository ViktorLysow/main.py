# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Hauptprogramm
# Autor: Viktor Lysow
# Letzte Änderung: 12.03.2021
# Zweck: Steuerung des gesamten Spielablaufs - dieses Programm muss gestartet werden, um das Spiel zu spielen.

import pygame
from screen import screen
from button import button

hintergrundstart1 = pygame.image.load("Bilder\Start\Start1.png")

x_Mitte = 348

y_NeuesSpiel = 250
y_Ende = 400

gruenDunkel = (0, 150, 0)
gruenHell = (0, 255, 0)

rotDunkel = (150, 0, 0)
rotHell = (255, 0, 0)

breite = 120
hoehe = 60

randDicke = 1

def start():                                                                    #Startbildschrim
    screen.blit(hintergrundstart1, (0, 0))

    maus = pygame.mouse.get_pos()
    klick = pygame.mouse.get_pressed()

    neuesSpeiel = button(x_Mitte, y_NeuesSpiel, "Neues Spiel", breite, hoehe, gruenDunkel, gruenHell, randDicke, maus, klick)      #Neues Spiel hat einen Returnwert
    button(x_Mitte, y_Ende, "Ende", breite, hoehe, rotDunkel, rotHell, randDicke, maus, klick)                                 #Ende hat keinen Returnwert

    if neuesSpeiel:
        del maus
        del klick
    return neuesSpeiel