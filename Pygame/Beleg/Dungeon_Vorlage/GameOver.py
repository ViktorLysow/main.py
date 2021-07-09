import pygame
from screen import screen

#Hier kommt der Game Over Hintegrund und dann wird alles für den Startbildschirm eingestellt bzw zurück gestellt

def gameOver():
    screen.blit(pygame.image.load("Bilder\GameOver.png"), (0, 0))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound/level.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    level = 0
    return level