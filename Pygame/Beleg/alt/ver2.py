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

linkeWand = pygame.draw.rect(screen, (0,0,0), (0,0,48,624),0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (816,0,-48,624),0)
obenWand = pygame.draw.rect(screen, (0,0,0), (0,0,816,48),0)
untenWand = pygame.draw.rect(screen,(0,0,0),(0,624,816,-48),0)

def zeichnen():
    screen.blit(hintergrund, (0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, breite, hoehe))
    pygame.display.update()

go = True

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    spielerRechteck = pygame.Rect(x, y, 48, 48)

    gedrueckt = pygame.key.get_pressed()

    if gedrueckt[pygame.K_UP] and not spielerRechteck.colliderect(obenWand):
        y -= geschw
    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        x += geschw
    if gedrueckt[pygame.K_DOWN] and not spielerRechteck.colliderect(untenWand):
        y += geschw
    if gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        x -= geschw

    zeichnen()
    clock.tick(60)