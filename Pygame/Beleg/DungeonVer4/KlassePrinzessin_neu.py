import pygame
from screen import screen
from KlasseMonster import Monster
from random import randint
from time import time
import sounds

class Prinzessin(Monster):
    def __init__(self, x, y, geschw, breite, level, hoehe, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, level, hoehe, bildFigur, zeitMonster)
        self.zeitGameOver = 0


    def fähigkeit(self):
        self.priSterben()

    def priSterben(self):
        if not self.Leben:
            self.heldTot = True

