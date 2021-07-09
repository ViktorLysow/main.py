# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Levelmanagement-Klasse
# Autor: Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Speichern des aktuellen Levels als static Klassenvariable
 
class LevelManagement:
    Level = 0                       # static!!
    def __init__(self):
        LevelManagement.Level = 0