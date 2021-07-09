import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Bilder\Karte\Level1.png")
screen = pygame.display.set_mode([816,624])
clock = pygame.time.Clock()
pygame.display.set_caption("ver1")

x = 300
y = 300

geschw = 3
breite = 48
hoehe = 48


def zeichnen():
    screen.blit(hintergrund, (0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, breite, hoehe))
    pygame.display.update()

go = True

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_UP]:
        y -= geschw
    if gedrueckt[pygame.K_RIGHT]:
        x += geschw
    if gedrueckt[pygame.K_DOWN]:
        y += geschw
    if gedrueckt[pygame.K_LEFT]:
        x -= geschw

    zeichnen()
    clock.tick(60)