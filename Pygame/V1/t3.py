import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Grafik/hintergrund.png")
screen = pygame.display.set_mode([1200, 595])
clock = pygame.time.Clock()
pygame.display.set_caption("test")

stehen = pygame.image.load("Grafik/stand.png")
sprung = pygame.image.load("Grafik/sprung.png")

rechtsGehen = [pygame.image.load("Grafik/rechts1.png"), pygame.image.load("Grafik/rechts2.png"),
               pygame.image.load("Grafik/rechts3.png"), pygame.image.load("Grafik/rechts4.png"),
               pygame.image.load("Grafik/rechts5.png"), pygame.image.load("Grafik/rechts6.png"),
               pygame.image.load("Grafik/rechts7.png"), pygame.image.load("Grafik/rechts8.png")]

linksGehen = [pygame.image.load("Grafik/links1.png"), pygame.image.load("Grafik/links2.png"),
              pygame.image.load("Grafik/links3.png"), pygame.image.load("Grafik/links4.png"),
              pygame.image.load("Grafik/links5.png"), pygame.image.load("Grafik/links6.png"),
              pygame.image.load("Grafik/links7.png"), pygame.image.load("Grafik/links8.png")]

sprungSound = pygame.mixer.Sound("sound/sprung.wav")

x = 300
y = 393

geschw = 3
breite = 40
hoehe = 80

linkeWand = pygame.draw.rect(screen, (0, 0, 0), (-2, 0, 2, 600), 0)
rechteWand = pygame.draw.rect(screen, (0, 0, 0), (1201, 0, 2, 600), 0)


def zeichnen(liste):
    global schritteRechts, schritteLinks
    screen.blit(hintergrund, (0, 0))

    if schritteRechts == 63:
        schritteRechts = 0
    if schritteLinks == 63:
        schritteLinks = 0

    if liste[0]:
        screen.blit(linksGehen[schritteLinks // 8], (x, y))

    if liste[1]:
        screen.blit(rechtsGehen[schritteRechts // 8], (x, y))

    if liste[2]:
        screen.blit(stehen, (x, y))

    if liste[3]:
        screen.blit(sprung, (x, y))

    pygame.display.update()


go = True
sprungvar = -16
richtg = [0, 0, 0, 0]
schritteRechts = 0
schritteLinks = 0

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    spielerRechteck = pygame.Rect(x, y, 96, 128)

    gedrueckt = pygame.key.get_pressed()
    richtg = [0, 0, 1, 0]
    if gedrueckt[pygame.K_UP] and sprungvar == -16:
        sprungvar = 15
        pygame.mixer.Sound.play(sprungSound)

    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        x += geschw
        richtg = [0, 1, 0, 0]
        schritteRechts += 1
    if gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        x -= geschw
        richtg = [1, 0, 0, 0]
        schritteLinks += 1

    if sprungvar >= -15:
        richtg = [0, 0, 0, 1]
        n = 1
        if sprungvar < 0:
            n = -1
        y -= (sprungvar ** 2) * 0.2 * n
        sprungvar -= 1

    if richtg[2] or richtg[3]:
        schritteRechts = 0
        schritteLinks = 0

    zeichnen(richtg)
    clock.tick(60)
