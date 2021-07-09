# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Boss-Klasse
# Autor: Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Boss-Entität definieren
# 
# Klasse Boss erbt alles von Geist
# kann in vier Richtungen schießen

class Boss ():
    def __init__(self):
        print("Hier Boss implementieren")
        self.leben = True # ohne dieses Attribut kann die Prinzessin nicht laufen. Kann entfernt werden, wenn von Geist geerbt wird.

        x = True
        while True:
            if x:
                #magie 1
                x = False
            else:
                #magie 2
                x = True


    def faehigkeit(self):                                                            #Alle Fähigkeiten von Monster kommen hier rein
        self.toeten()
        self.funk()