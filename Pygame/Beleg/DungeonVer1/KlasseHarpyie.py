from KlasseMonster import Monster
from hindernise import grenzeLevel

class Harpyie (Monster):                                                            #Harpyie soll in allen 4 Richtungen hin und wieder schißen
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)

    def hindernis(self,richtung):                                                   #kann über Lava fliegen
        r = True
        for i in grenzeLevel[2]:
            if richtung.colliderect(i):
                r = False
        return r