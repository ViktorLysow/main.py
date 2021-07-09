import pygame
import sys
import sounds
from screen import screen
from screen import font

aktivButton = False

def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(bx, by, nachricht, laenge, hoehe, farbe_normal, farbe_aktiv, randDicke, maus, klick):    # irgendwo aus dem internet :)
    global aktivButton
    if maus[0] > bx and maus[0] < bx + laenge and maus[1] > by and maus[1] < by + hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx, by, laenge, hoehe))
        if klick[0] == 1 and aktivButton == False:
            aktivButton = True
            if nachricht == "Neues Spiel":

                pygame.mixer.Sound.play(sounds.soundTor())
                pygame.time.wait(1000)
                return True
            elif nachricht == "Ende":
                sys.exit()
        if klick[0] == 0:
            aktivButton = False
    else:
        pygame.draw.rect(screen, farbe_normal, (bx, by, laenge, hoehe))
    pygame.draw.rect(screen, (0, 0, 0), (bx, by, laenge, hoehe), randDicke)
    textGrund, textKasten = textObjekt(nachricht, font)
    textKasten.center = ((bx + (laenge / 2)), (by + (hoehe / 2)))
    screen.blit(textGrund, textKasten)
    return False