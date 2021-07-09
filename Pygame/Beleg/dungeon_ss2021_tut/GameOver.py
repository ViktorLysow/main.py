# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Game Over
# Autor: Viktor Lysow
# Letzte Änderung: 04.03.2021
# Zweck: Festlegung was passieren soll, wenn das Spiel verloren wurde
 
from screen import screen
import pygame
import DatenSammeln as ds                                                   # Für den Matlab Beleg
from screen import screen

#Hier kommt der Game Over Hintegrund und dann wird alles für den Startbildschirm eingestellt bzw zurück gestellt

def gameOver(spieler):
    screen.blit(pygame.image.load("Bilder\GameOver.png"), (0, 0))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound/level.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    level = 0
    ds.daten_csv(3, spieler.schritteZaehler)                              # Anzahl der Schritte wird gespeichert (für Matlab)
    ds.daten_csv(4, spieler.schussZaehler)                                # Schusszahl wird gespeichert (für Matlab)
    ds.write_csv()                                                        # csv Datei wird erstellt oder überschrieben (für Matlab)
    spieler.schritteZaehler = 0
    spieler.schussZaehler = 0
    return level