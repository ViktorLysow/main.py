import pygame

def soundTor():
    soundtor = pygame.mixer.Sound("Sound/tor.wav")
    soundtor.set_volume(0.5)
    return soundtor

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