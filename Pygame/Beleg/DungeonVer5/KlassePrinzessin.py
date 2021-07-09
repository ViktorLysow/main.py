import pygame
from screen import screen
from KlasseMonster import Monster
from time import time
import sounds

# Prinzessin erbt Alles von Monster
# Held stirbt wenn Prinzessin stirbt
# Prinzesin kann Emotionen zeigen

class Prinzessin(Monster):
    def __init__(self, x, y, geschw, breite, level, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, level, hoehe, bildFigur, zeitMonster)
        self.emotionWechsel = 0
        self.bildAngst = [pygame.image.load(f"Bilder/Emotion/!1.png"),
                          pygame.image.load(f"Bilder/Emotion/!2.png"),
                          pygame.image.load(f"Bilder/Emotion/!3.png")]
        self.bildHerz = [pygame.image.load(f"Bilder/Emotion/Herz1.png"),
                         pygame.image.load(f"Bilder/Emotion/Herz2.png"),
                         pygame.image.load(f"Bilder/Emotion/Herz3.png")]
        self.zeitEmotion = zeitMonster

    def faehigkeit(self):                                                                    #Fähigkeiten von Monster werden mit den Fähigkeiten der Klasse überschrieben!!!
        self.priSterben()
        if self.monsterDaten.leben:                                                         #wechselt Emotion je nach ob der Endboss lebt oder nicht
            self.emotion(self.bildAngst)
        else:
            self.emotion(self.bildHerz)

    def priSterben(self):                                                                   # Held stirbt, wenn Prinzessin stirbt
        if not self.leben:
            sounds.soundTot()
            screen.blit(self.bildTot[self.feuerWechsel], (self.x, self.y))
            screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
            self.heldTot = True

    def emotion(self, emo):                                                                 # Zeigt eine Sprechblase über dem Kopf
        screen.blit(emo[self.emotionWechsel], (self.x, self.y - 48))
        if time() - self.zeitEmotion >= 0.15:                                               #Animation der Sprechblase
            if self.emotionWechsel < 2:
                self.emotionWechsel += 1
            else:
                self.emotionWechsel = 0
            self.zeitEmotion = time()