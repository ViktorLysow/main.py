# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Pygame-Fenster
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Aktivierung von Pygame mit entsprechenden Parametern

import pygame

pygame.init()

screen = pygame.display.set_mode([816, 624])
clock = pygame.time.Clock()
pygame.display.set_caption("Dungeon v2021 Hochschule Anhalt, by Viktor Lysow and Johannes Tümler") # Sie dürfen sich hier hinzufügen
font = pygame.font.SysFont('Impact', 20)

feld = 48   # pixel