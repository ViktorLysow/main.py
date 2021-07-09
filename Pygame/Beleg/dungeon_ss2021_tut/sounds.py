# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Sounds
# Autor: Viktor Lysow
# Letzte Änderung: 03.02.2021
# Zweck: Verwaltung der Soundfiles

import pygame

#Hier werden alle Geräusche aufgelistet

def soundTor():
    soundtor = pygame.mixer.Sound("Sound/tor.wav")
    soundtor.set_volume(0.5)
    pygame.mixer.Sound.play(soundtor)

def soundFeuer():
    soundFeuer = pygame.mixer.Sound("Sound/Fire.wav")
    soundFeuer.set_volume(0.5)
    pygame.mixer.Sound.play(soundFeuer)

def soundMagie():
    soundMagie = pygame.mixer.Sound("Sound/Attack2.wav")
    soundMagie.set_volume(0.5)
    pygame.mixer.Sound.play(soundMagie)

def soundKolMag():
    soundKolMag = pygame.mixer.Sound("Sound/mag.wav")
    soundKolMag.set_volume(0.5)
    pygame.mixer.Sound.play(soundKolMag)

def soundTot():
    soundTot = pygame.mixer.Sound("Sound/tot.wav")
    soundTot.set_volume(0.5)
    pygame.mixer.Sound.play(soundTot)

def soundGewonne():
    soundTot = pygame.mixer.Sound("Sound/Victory1.wav")
    soundTot.set_volume(0.5)
    pygame.mixer.Sound.play(soundTot)

def soundLevel():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound/level.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)

def soundBoss():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound/levelBoss.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.6)