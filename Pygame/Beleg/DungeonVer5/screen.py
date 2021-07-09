import pygame

pygame.init()

screen = pygame.display.set_mode([816, 624])
clock = pygame.time.Clock()
pygame.display.set_caption("Dungeon")
font = pygame.font.SysFont('Impact', 20)

feld = 48   # pixel