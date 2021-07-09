from KlasseGeist import Geist
from KlasseHarpyie import Harpyie



class Boss (Geist, Harpyie):       #Boss soll alle Monster fähigkeiten haben + vielleicht noch eine
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur,zeitMonster)
        self.MonsterDupl = Harpyie


    def fähigkeit(self):
        self.toeten()
        self.duplizieren()
        self.schissen()