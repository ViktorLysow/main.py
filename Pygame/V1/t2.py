import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Grafik\hintergrund.png")
screen = pygame.display.set_mode([1200,595])
clock = pygame.time.Clock()
pygame.display.set_caption("test")


stehen = pygame.image.load("Grafik\stand.png")
sprung = pygame.image.load("Grafik\sprung.png")

x = 300
y = 440

geschw = 3
breite = 40
hoehe = 80

linkeWand = pygame.draw.rect(screen, (0,0,0), (-2,0,2,600),0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1201,0,2,600),0)

def zeichnen():
    screen.blit(hintergrund, (0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, breite, hoehe))
    pygame.display.update()

go = True
sprungvar = -16
richtg = [0,0,0,0]



while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    spielerRechteck = pygame.Rect(x, y, 40, 80)

    gedrueckt = pygame.key.get_pressed()

    if gedrueckt[pygame.K_UP] and sprungvar == -16:
        sprungvar = 15
    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        x += geschw
    if gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        x -= geschw

    if sprungvar >= -15:
        n = 1
        if sprungvar < 0:
            n = -1
        y -=(sprungvar**2)*0.17*n
        sprungvar -= 1

    zeichnen()
    clock.tick(60)