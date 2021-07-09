import pygame
import sys
import sounds
from screen import screen
from screen import font

aktivButton = False

def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(bx, by, nachricht, breite, hoehe, farbe_normal, farbe_aktiv, randDicke, maus, klick):
    global aktivButton

    if maus[0] > bx and maus[0] < bx + breite and maus[1] > by and maus[1] < by + hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx, by, breite, hoehe))
        if klick[0] == 1 and aktivButton == False:
            aktivButton = True

            if nachricht == "Neues Spiel":
                sounds.soundTor()
                pygame.time.wait(1000)
                return True

            elif nachricht == "Ende":
                sys.exit()

        if klick[0] == 0:
            aktivButton = False

    else:
        pygame.draw.rect(screen, farbe_normal, (bx, by, breite, hoehe))
    pygame.draw.rect(screen, (0, 0, 0), (bx, by, breite, hoehe), randDicke)
    textGrund, textKasten = textObjekt(nachricht, font)
    textKasten.center = ((bx + (breite / 2)), (by + (hoehe / 2)))
    screen.blit(textGrund, textKasten)
    return False