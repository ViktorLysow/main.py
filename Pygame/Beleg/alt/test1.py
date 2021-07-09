import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont('Impact', 20)


def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()


def testmethode():
    for x in range(0, 3):
        print(x)


aktiv = False


def button(bx, by, nachricht, laenge, hoehe, farbe_normal, farbe_aktiv, randDicke):
    global aktiv
    if maus[0] > bx and maus[0] < bx + laenge and maus[1] > by and maus[1] < by + hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx, by, laenge, hoehe))
        if klick[0] == 1 and aktiv == False:
            aktiv = True
            if nachricht == "START":
                testmethode()
            elif nachricht == "STOP":
                sys.exit()
        if klick[0] == 0:
            aktiv = False
    else:
        pygame.draw.rect(screen, farbe_normal, (bx, by, laenge, hoehe))
    pygame.draw.rect(screen, (0, 0, 0), (bx, by, laenge, hoehe), randDicke)
    textGrund, textKasten = textObjekt(nachricht, font)
    textKasten.center = ((bx + (laenge / 2)), (by + (hoehe / 2)))
    screen.blit(textGrund, textKasten)


go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((255, 255, 255))
    maus = pygame.mouse.get_pos()
    klick = pygame.mouse.get_pressed()
    button(150, 170, "Neues Spiel", 120, 60, (0, 150, 0), (0, 255, 0), 1)
    button(350, 170, "Ende", 120, 60, (150, 0, 0), (255, 0, 0), 1)
    pygame.display.flip()
    pygame.time.wait(10)