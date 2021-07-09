import pygame

def soundTor():
    soundtor = pygame.mixer.Sound("Sound/tor.wav")
    soundtor.set_volume(0.5)
    return soundtor

def soundFeuer():
    soundFeuer = pygame.mixer.Sound("Sound/Fire.wav")
    soundFeuer.set_volume(0.5)
    return soundFeuer

def soundMagie():
    soundMagie = pygame.mixer.Sound("Sound/Attack2.wav")
    soundMagie.set_volume(0.5)
    return soundMagie

def soundKolMag():
    soundKolMag = pygame.mixer.Sound("Sound/mag.wav")
    soundKolMag.set_volume(0.5)
    return soundKolMag

def soundTot():
    soundTot = pygame.mixer.Sound("Sound/tot.wav")
    soundTot.set_volume(0.5)
    return soundTot

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