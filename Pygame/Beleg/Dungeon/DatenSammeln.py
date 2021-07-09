#Daten für den Matlab Beleg
#war für Pandas zu blöd
import datetime

dateiName = 'Spiel_Daten.csv'

zeile0 = ['0','Datum','Uhrzeit','Schritte Held', 'Schüsse Held´', 'Zeit Level 1', 'Zeit Level2', 'Zeit Level3', 'Gesamt Zeit', 'Besiegt in Level']   #Text Zeile
neue_zeile =[0,0,0,0,0,0,0,0,0,0]                                                                                                                   #Zeile, die eingefügt wird

def open_csv():

    try:                                                                                                                                            #Test, ob die csv existiert
        op_text = open(dateiName)
    except:                                                                                                                                         #Wenn nicht, neu erstellen
        neu_text = open(dateiName, 'w')
        neu_text.write(f'{zeile0[0]};{zeile0[1]};{zeile0[2]};{zeile0[3]};{zeile0[4]};{zeile0[5]};{zeile0[6]};{zeile0[7]};{zeile0[8]};{zeile0[9]}')
        neu_text.close()
        op_text = open(dateiName)

    text = op_text.read()
    op_text.close()

    zeilen = text.split('\n')
    tabelle = []
    if not zeilen == ['']:
        for i in range(len(zeilen)):
            spalten = zeilen[i].split(';')
            tabelle.append(spalten)

    neue_zeile[0] = len(zeilen)                                                   #Index für die eingetragenen Informationen (kann eigentlich weg)

    return tabelle

def daten_csv(spalte, info):       # (welche Spalte, die Information in der Spalte)  Zeit, Schritte und Schüsse werden hier übergeben

    info = str(info)

    neue_zeile[spalte] = info


def write_csv():                   # Die csv wird hier überschrieben (Speichern)
    neue_zeile[1] = datetime.date.today()                                           #Datum in Spalte 2
    neue_zeile[2] = datetime.datetime.now().strftime('%H:%M:%S')                    #Uhrzeit in Spalte 3

    tabelle = open_csv()                                                            #Gesamte Tabelle
    tabelle.append(neue_zeile)                                                      #Gesmate Tabelle + der neuen Zeile

    neu_text = open(dateiName, 'w')

    for i in range(len(tabelle)):
        neu_text.write(f'{tabelle[i][0]};{tabelle[i][1]};{tabelle[i][2]};{tabelle[i][3]};{tabelle[i][4]};{tabelle[i][5]};{tabelle[i][6]};{tabelle[i][7]};{tabelle[i][8]};{tabelle[i][9]}')
        if not len(tabelle) - 1 == i:
            neu_text.write('\n')

    neu_text.close()
    reset()

def reset():                                                                       #neue Zeile wird wieder auf 0 gesetzt für das eventuelle nächste Spiel
    global neue_zeile
    neue_zeile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
