##### Der nachfolgende Quelltext unterliegt der "CC BY-NC-ND 4.0" Lizenz.
##### Kommerzielle Nutzung, Modifikation und Distribution ohne Namensnennung sind strengstens untersagt.
##### © Laurenz Brause und Daniel Pauli 2022

# Wie bei jedem Programm, werden zuerst die Bibliotheken (Module) importiert.
import random
import gc
import pygame

# Das Wesen wird als Objekt initiiert
class Wesen(object):
    # Die Genomgröße beschreibt die Größe des Erbguts.
    # Je höher die Genomgröße, desto mehr Genome und höher die Komplexität des Lebewesens.
    # (Einheit: Mbp = Megabasenpaare (Gegenüberliegende Nukleobasen (Guanin, Thymin, Cytosin, Adenin) auf der DNA), 
    # der Mensch hat 3200 Mbp (Genomgröße = 3200)
    # Pneumokokken haben 2,2 Mbp, kommen unserem Modell also sehr nahe)
    def __init__(self, GenomGröße):
        # Jedes Wesen besitzt eine Liste an Genen, in der das x_Gen, y_Gen und z_Gen gespeichert sind
        # (Somit das Erbgut des Wesens)
        self.Gene = []
        # Eine temporäre Variable, die den Wert der Genomgröße annimmt, wird initialisiert
        Temp = GenomGröße
        while Temp > 0:
            # Da das ein Wesen nur zufällige Gene erhalten soll, wenn die Simulation startet,
            # wird überprüft, dass die Generationenanzahl höchtens bei 1 liegt (dass es die erste Generation ist)
            # und, dass es keine Überlebende gibt. (Da es die erste Generation ist, kann es keine Überlebende geben)
            if Generation[0] <= 1 or len(Überlebende) == 0:
                # Die folgenden, zufälligen Gene werden der "Gene"-Liste des Wesens angehängt.
                self.Gene.append(
                    #    x0_gen (zufälliger Wert: entweder 0 oder 1)
                    Genom([random.randrange(2),
                    #    x1_gen (zufälliger Wert: entweder 0 oder 1)
                          random.randrange(2)],
                    #    y0_gen (zufälliger Wert: zwischen 0 und 7)
                         [random.randrange(8),
                    #    y1_gen (zufälliger Wert: zwischen 0 und 7)
                          random.randrange(8)], 
                    #    z_gen (zufälliger Wert: zwischen 0 und 8)
                         random.randrange(9)))
            # Die temporäre Variable wird um 1 verringert, nachdem ein Genom (ein Datensatz aus x0-,x1-,y0-,y1-,z-Gen) hinzugefügt wurde.
            # Das Hinzufügen der zufälligen Gene wird solange wiederholt, bis der temporäre Wert 0 beträgt.
            # Somit entspricht letztendlich die Anzahl der erschaffenen Genome (mit zufälligen Genen) der festgelegten Genomgröße.
            Temp -= 1
        # Die Position ist eine Liste mit einem zufälligen Wert von 0 bis zur Breite, bzw. Höhe des Simulationsfensters.
        # Somit wird die x- und y-Koordinate abgespeichert.
        self.pos = [random.randrange(Größe[0]), random.randrange(Größe[1])]


# Für das Handling jedes einzelnen Gens wird dieses Objekt initiiert
class Genom(object):

    def __init__(self, x_gen, y_gen, z_gen):
        # Das Wesen hat 3 verschiedene Genarten
        # x_gen, y_gen, z_gen
        self.x_gen = x_gen
        self.y_gen = y_gen
        self.z_gen = z_gen
        # Bei einer Chance von 1 zu 50 mutiert das Gen. (Wahrscheinlickeit von 2%)
           
    def mutation(self):
        # Der Mutationswert ist ein zufälliger Wert zwischen 0 und 15, 
        # der darüber entscheidet, welches Gen mutiert.
        MutationsWert = random.randrange(16)
        if MutationsWert < 2:
        # Wenn der Mutationswert 0 oder 1 beträgt 
        # (mit einer Wahrscheinlichkeit von 6,25%), 
        # erhält das jeweilige x-Gen entweder den neuen Wert 0 oder 1
            self.x_gen[MutationsWert] = random.randrange(2)
        elif MutationsWert >= 2 and MutationsWert < 5:
        # Wenn der Mutationswert zwischen 2 und 4 liegt
        # (mit einer Wahrscheinlichkeit von 18,75%),
        # erhält das y0-Gen einen zufälligen Wert zwischen 0 und 7
            self.y_gen[0] = random.randrange(8)
        elif MutationsWert >= 5 and MutationsWert < 8:
        # Wenn der Mutationswert zwischen 5 und 7 liegt
        # (mit einer Wahrscheinlichkeit von 18,75%),
        # erhält das y1-Gen einen zufälligen Wert zwischen 0 und 7
            self.y_gen[1] = random.randrange(8)
        # Mit einer Wahrscheinlichkeit von 50% 
        # erhält das z_Gen einen zufälligen Wert zwischen 0 und 8
        else:
            self.z_gen = random.randrange(9)

# Um die Wesen zu generieren
def generieren():
    # Um die festgelegte Anzahl an Wesen zu generieren, 
    # wird ein temporärer Wert mit dieser Anzahl initialisiert.
    Temp = GesamtAnzahl
    # Solange der temporäre Wert größer 0 ist, werden Wesen mit der festgelegten Genomgröße erschaffen.
    while Temp > 0:
        WesenListe.append(Wesen(GenomGröße))
        # Nachdem ein Wesen erschaffen wurde, wird der temporäre Wert um 1 verringert.
        Temp -= 1

# Render Funktion
def renderFenster(Fenster):
    # Der Hintergrund wird grau gefärbt.
    Fenster.fill((50, 50, 50))
    # Das Simulationsfenster wird gerendert.
    # Damit es an die Fenstergröße angepasst ist, wird es 8x so groß gemacht.
    # pygame.draw.rect(Fenster, (r,g,b), (Position_x(Abstand vom linken Rand), Position_y(Abstand vom oberen Rand), Breite, Höhe))
    pygame.draw.rect(Fenster, (0, 0, 0), (29, 29, Größe[0] * 8 + 1, Größe[1] * 8 + 1))
    for x, zielpunkt_der_safezone in enumerate(Safezone):
        # Die Safezone wird gerendert
        # Die Größe ist an die des gesamten Fensters angepasst
        pygame.draw.rect(Fenster, (0, 100, 0), (30 + zielpunkt_der_safezone[0] * 8, 30 + zielpunkt_der_safezone[1] * 8, 7, 7))

    # Hiermit wird der Schweif hinter dem Wesen gerendert.
    # i markiert den Index der jeweiligen Position in der Liste der gespeicherten Positionen 
    # und PositionsListenWerte den Wert (also die Positionsdaten x, y).
    for i, PositionsListenWerte in enumerate(PositionsListe):
        # Die Positionsdaten (also PositionsListenWerte) werden enumeriert und das Ganze in "altePosition" gespeichert,
        # da diese Position nun nicht mehr aktuell ist.
        for j, altePosition in enumerate(PositionsListenWerte):
            # Je nachdem, welchen Index die Position hat, wird sie dunkler/heller gefärbt.
            # Der erste gespeicherte Wert (die älteste Position) wird mit i=0 bezeichnet.
            # Also beträgt der Farbwert (5 + 0*10).
            # Somit ist der RGB Wert ((5+0*10),(5+0*10),(5+0*10)) also (5,5,5).
            # Je neuer die gespeicherte Position ist (also desto näher er an der aktuellen Position liegt), 
            # desto heller wird sie gerendert.
            # Somit wird der aktuellste gespeicherte Wert mit i = 7 bezeichnet.
            # Also ist der RGB Wert ((5+7*10),(5+7*10),(5+7*10)) also (75,75,75), welcher definitiv heller ist als (5,5,5).
            # Die altePosition wird mit dem Faktor 8 und dem Summanden 30 an die Größe des Fensters angepasst.
            # Und anschließend wird jede altePosition in ihrer Farbe gerendert.
            # So entsteht ein Schweif, der, je weiter er vom Wesen entfernt ist, dunkler wird.
            pygame.draw.rect(Fenster, (5 + i * 10, 5 + i * 10, 5 + i * 10), (30 + altePosition[0] * 8, 30 + altePosition[1] * 8, 7, 7))
            
    # Nun wird die Bewegung der Wesen visualisiert.
    LoopZähler = 7
    # Jede Position des Wesens wird an der Stelle 0 der PositionsListe (PositionsListe[0]) gespeichert.
    # Jedes Mal, wenn eine neue Position dazukommt, wird die vorige Position um einen Index nach vorne "verschoben".
    # Die Liste kann 8 Elemente beinhalten und die Nummerierung beginnt bei 0.
    # Deshalb trägt der LoopZähler den Wert 7.
    while LoopZähler > 0:
        # Solange der LoopZähler größer 0 ist, wird jede gespeicherte Position um 1 nach vorne "verschoben".
        PositionsListe[7 - LoopZähler] = PositionsListe[8 - LoopZähler]
        LoopZähler -= 1
    # Anschließend wird die Position an letzter Stelle gelöscht, sodass Platz für eine neue Position vorhanden ist.
    PositionsListe[7] = []
    
    # Daraufhin werden die Wesen eingefärbt.
    for i, Wesen in enumerate(WesenListe):
        # Die Standardfarbe ist grau.
        farbe = [125, 125, 125]
        FunktionellesGenom = 0
        # Für jedes x_Gen[1], das den Wert 1 hat, wird das Genom als funktionell deklariert, 
        # da das x1-Gen dafür verantwortlich ist, dass die Veränderung im stabilen Wert gespeichert wird.
        # Das bedeutet, dass Wesen mit mehr funktionellen Genen eine hellere Farbe haben.
        for j, genom in enumerate(Wesen.Gene):
            if genom.x_gen[1] == 1:
                FunktionellesGenom += 1
        # Durch die Berechnungen erhält man nie einen Wert, der außerhalb des RGB-Farbspektrums liegt.
        # Die nachfolgenden Minima und Maxima wurden durch genaueste Feinjustierung ermittelt.
        # Sie funktionieren für jegliche Genomgrößen!
        for j, genom in enumerate(Wesen.Gene):
            if genom.x_gen[1] == 1 and genom.y_gen[1] == 0:
                farbe[0] += min(254 - farbe[0], int(40 + abs(genom.z_gen * 60)) * 2 / FunktionellesGenom)
            if genom.x_gen[1] == 1 and genom.y_gen[1] == 1:
                farbe[0] -= min(farbe[0], int(40 + abs(genom.z_gen * 60)) * 2 / FunktionellesGenom)
            if genom.x_gen[1] == 1 and genom.y_gen[1] == 2:
                farbe[1] += min(254 - farbe[1], int(40 + abs(genom.z_gen)) * 2 / FunktionellesGenom)
            if genom.x_gen[1] == 1 and genom.y_gen[1] == 3:
                farbe[1] -= min(farbe[1], int(40 + abs(genom.z_gen * 60)) * 2 / FunktionellesGenom)
            if genom.x_gen[1] == 1 and genom.y_gen[1] == 4:
                farbe[2] += max(-farbe[2], min(254 - farbe[2], (80 + genom.z_gen * 60) / FunktionellesGenom))
        # Alle Wesen werden gerendert                                            (Passende x und y Position im Fenster),        passende Breite und Höhe
        pygame.draw.rect(Fenster, (int(farbe[0]), int(farbe[1]), int(farbe[2])), (30 + Wesen.pos[0] * 8, 30 + Wesen.pos[1] * 8, 7, 7))
        # Die aktuellste Position der Wesen wird nun an letzter Stelle der PositionsListe gespeichert.
        PositionsListe[7].append([Wesen.pos[0], Wesen.pos[1]])
        
    # Um immer genau zu wissen, in welcher Generation die Simulation sich gerade befindet, 
    # wird an den oberen rechten Rand ein Indikator hinzugefügt.
    
    # Die Schriftart (keine Besondere) und Größe werden festgelegt
    generationsIndikator = pygame.font.Font(None, 30)
    # Es soll: "Generation: (Generationenanzahl)" in Orange geschrieben werden.
    # Das True bezieht sich auf Antialiasing. Damit werden unerwünschte Pixel, die durch das Pixelraster entstehen, vermindert.
    # Der Text ist geglättet und nicht verpixelt
    generationsRendering = generationsIndikator.render("Generation:" + str(Generation[0]), True, (255, 120, 0))
    # Der Text wird oben rechts über dem Simulationsfenster geschrieben.
    Fenster.blit(generationsRendering, generationsRendering.get_rect(center=(Größe[0] * 8 + 59 - 90, 20)))
    # Nachdem alles gerendert wurde, wird das gesamte Pygamefenster neugeladen.
    pygame.display.update()

# Diese Funktion wird am Ende einer Generation aufgerufen.
def GenerationsEnde():
    # Da die WesenListe und die Liste der Überlebenden bearbeitet werden und das für den Start der nächsten Generation von Bedeutung ist,
    # werden diese in dieser Funktion als global deklariert.
    global WesenListe, Überlebende
    # Sollte das Pygamefenster geschlossen werden, wird die Simulation abgebrochen.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Überprüfung, ob die Ticks der Generation abgelaufen sind.
    if Generation[1] < 0:
        # Die nicht mehr genutzten Objekte werden durch den Garbage Collecter gelöscht, sodass der Arbeitsspeicher entlastet wird.
        gc.collect()
        # Die Generationenanzahl wird um 1 erhöht.
        Generation[0] += 1
        # Die ablaufenden Ticks werden wieder auf 200 gesetzt.
        Generation[1] = Generation[2]
        # Eine neue Liste mit den überlebenden Wesen, die es in die Safezone geschafft haben, wird initialisiert.
        Überlebende = []
        for i, creature in enumerate(WesenListe):
            for x, Safespot in enumerate(Safezone):
                # Bei jedem Wesen wird geprüft, ob die Koordinaten mit denen der Safezone übereinstimmen.
                if creature.pos[0] == Safespot[0] and creature.pos[1] == Safespot[1]:
                    # Wenn alles zutrifft, wird ein neues Wesen erschaffen.
                    # Dieses Wesen wird ohne anfängliche zufällige Gene erschaffen.
                    neuesWesen = Wesen(0)
                    for j, genom in enumerate(creature.Gene):
                        # Das überlebende Wesen vererbt seine Gene an das neu erschaffene Wesen.
                        neuesWesen.Gene.append(Genom([genom.x_gen[0], genom.x_gen[1]], [genom.y_gen[0], genom.y_gen[1]], genom.z_gen))
                    # Somit lässt sich eine Liste der Überlebenden mitsamt ihren Genen erstellen.
                    Überlebende.append(neuesWesen)
        # Die Liste der Wesen wird nach jeder Generation geleert.
        WesenListe = []
        # Die Anzahl der Wesen in der Liste der Überlebenden wird ausgegeben.
        print('Anzahl der Überlebenden:' + str(len(Überlebende)))
        Temp = GesamtAnzahl
        # Für jedes der (in unserem Beispiel 200) Wesen 
        while Temp > 0:
            # wird ein Wesen aus der Liste der Überlebenden zufällig ausgewählt.
            AuserwähltesWesen = Überlebende[random.randrange(len(Überlebende))]
            neuesWesen = Wesen(0)
            for j, genom in enumerate(AuserwähltesWesen.Gene):
                # Und Erbinformationen (Bewegung, Farbe, etc.) werden an ein anderes Wesen weitergegeben.
                # Starke/gute Gene, mit denen ein Wesen in der vorigen Generation die Safezone erreicht hat, werden weitergegeben.
                neuesWesen.Gene.append(Genom([genom.x_gen[0], genom.x_gen[1]], [genom.y_gen[0], genom.y_gen[1]], genom.z_gen))
            # Das neue Wesen wird zur Liste der Wesen hinzugefügt, die in der nächsten Generation die Safezone erreichen müssen.
            WesenListe.append(neuesWesen)
            # Bis alle Wesen der Liste der Überlebenden enumeriert wurden, wird die Vererbung wiederholt.
            Temp -= 1
    # So lässt sich ein "Survival of the fittest" nach Charles Darwin simulieren.


# Mit dieser Funktion wird überprüft, ob die Position aller Wesen im Bereich des Fensters (zwischen 0 und 100) liegt
# und, dass sich auf dem Feld nicht bereits ein anderes Wesen befindet.
def überprüfeValidität(x, y):
    # Hier wird zuerst sichergegangen, dass die eingegebenen
    # Werte im Bereich des Simulationsfensters liegen.
    if x >= 0 and y >= 0 and x < Größe[0] and y < Größe[1]:
        for i, Wesen in enumerate(WesenListe):
            # Ist eine x-/y-Position eines Wesens
            # kongruent zu den eingegebenen Werten?
            if Wesen.pos[0] == x and Wesen.pos[1] == y:
                # Wenn ja, dann return False.
                # Die eingegebenen Werte sind keine validen Positionen.
                return False
        # Wenn nein, dann return False.
        # Die eingegebenen Werte sind valide Positionen.
        return True

# Diese Funktion wird am Anfang einer Generation aufgerufen.
# Sie beinhaltet die zufällige Bewegung der Wesen.
def simulationStart():
    # Als Voraussetzung wird gegeben, dass die ablaufenden Ticks über 0 liegen. (Also, dass die Simulation aktuell läuft.)
    if Generation[1] >= 0:
        for i, Wesen in enumerate(WesenListe):
            # Der stabile Wert wird initialisiert, eine der elementarsten Datenspeicherungen dieser Simulation.
            # Siehe Dokumentation, dort ist die Funktionsweise anschaulich erklärt.
            stabilerWert = [0, 0, 0, 0, 0, 0, 0, 0]
            for j, genom in enumerate(Wesen.Gene):
                # Hier kommt nun die Hauptbedingung: Das x_Gen muss 0 betragen.
                if genom.x_gen[0] == 0:
                    # Die Veränderung legt fest, wie die Position eines Wesens verändert werden soll.
                    # Sie hat viele Einflussfaktoren.
                    Veränderung = 0
                    # Die erste Abhängigkeit sind die Gene des Wesens.
                    # Je nachdem, welche vorhanden sind, werden unterschiedliche Eigenschaften der Veränderung hinzugefügt.
                    # Diese werden durch das z-Gen und die Größe auf die Größe des Fensters skaliert.
                    if genom.y_gen[0] == 0:
                        # Die y-Position des Wesens wird der Veränderung hinzugefügt.
                        Veränderung += Wesen.pos[1] * genom.z_gen / Größe[1] * 8
                    elif genom.y_gen[0] == 1:
                        # Die x-Position des Wesens wird der Veränderung hinzugefügt.
                        Veränderung += Wesen.pos[0] * genom.z_gen / Größe[0] * 8
                    elif genom.y_gen[0] == 2:
                        # Der aktuelle Zeitwert wird der Veränderung hinzugefügt.
                        Veränderung += Generation[1] * genom.z_gen / Generation[2] * 2
                    elif genom.y_gen[0] == 3:
                        # Die Tatsache, dass sich das Wesen in der Safezone befindet, wird als Wert (z-Gen / 2) der Veränderung hinzugefügt.
                        for x, zielpunkt_der_safezone in enumerate(Safezone):
                            if Wesen.pos[0] == zielpunkt_der_safezone[0] and Wesen.pos[1] == zielpunkt_der_safezone[1]:
                                Veränderung += genom.z_gen / 2
                    elif genom.y_gen[0] == 4:
                        # Ein zufälliger Wert wird der Veränderung hinzugefügt
                        Veränderung += (random.randrange(9) - 4) * genom.z_gen / 8
                    elif genom.y_gen[0] == 5:
                        Veränderung += (random.randrange(9) - 5) * genom.z_gen / 8

                    # Der veränderliche Wert wird im stabilen Wert gespeichert [0,0,0,0,0,0,0,0]
                    # Das x1_Gen entscheidet, ob die Veränderung gespeichert wird
                    # und daraufhin entscheidet das y1_Gen und x1-Gen über die Stelle, an der die Veränderung gespeichert wird.
                    if genom.x_gen[1] == 1:
                        stabilerWert[int(genom.y_gen[1] / (2 - genom.x_gen[1]))] += Veränderung

            # Diese Liste wird genutzt, um eine zufällige Bewegung zu ermöglichen.
            ZufälligeBewegungen = []

            # Die Liste des stabilenWertes wird enumeriert.
            for a, Ausführung in enumerate(stabilerWert):
                # und jeder Wert, mit einer zufälligen Zahl von 0 bis 39 multipliziert, der Liste angehängt.
                ZufälligeBewegungen.append(Ausführung * random.randrange(40))

            # Nun wird die Liste der Zuälligen Bewegungen enumeriert.
            for s, Aktion in enumerate(ZufälligeBewegungen):
                # Der Wert muss größer 0 sein und das Maximum der Werte aus der Liste der ZufälligenBewegungen.
                if Aktion > 0 and Aktion == max(
                        ZufälligeBewegungen[0], ZufälligeBewegungen[1],
                        ZufälligeBewegungen[2], ZufälligeBewegungen[3],
                        ZufälligeBewegungen[4], ZufälligeBewegungen[5],
                        ZufälligeBewegungen[6], ZufälligeBewegungen[7]):

                    # Nun kann die zufällige Bewegung erfolgen.
                    # An der Stelle in der Liste ZufälligeBewegungen, an der der Wert angehängt wurde, markiert s den Index [s=0,s=1,s=2,s=3,s=4,...].
                    # Je nachdem, welchen Wert s hat, bewegt sich das Wesen nach oben, unten, links, rechts oder einfach zufällig.

                    # Überprüfung, dass x - 1 immer noch im Bereich des Fensters liegt.
                    if s == 0 and überprüfeValidität(Wesen.pos[0] - 1,
                                                     Wesen.pos[1]):
                        # Bewegung nach links (um einen Schritt) (x - 1).
                        Wesen.pos[0] -= 1
                    # Überprüfung, dass x + 1 immer noch im Bereich des Fensters liegt.
                    elif s == 1 and überprüfeValidität(Wesen.pos[0] + 1,
                                                       Wesen.pos[1]):
                        # Bewegung nach rechts (um einen Schritt) (x + 1).
                        Wesen.pos[0] += 1
                    # Überprüfung, dass y - 1 immer noch im Bereich des Fensters liegt.
                    elif s == 2 and überprüfeValidität(Wesen.pos[0],
                                                       Wesen.pos[1] - 1):
                        # Bewegung nach oben (um einen Schritt) (y - 1).
                        Wesen.pos[1] -= 1
                    # Überprüfung, dass y + 1 immer noch im Bereich des Fensters liegt.
                    elif s == 3 and überprüfeValidität(Wesen.pos[0],
                                                       Wesen.pos[1] + 1):
                        # Bewegung nach unten (um einen Schritt) (y + 1).
                        Wesen.pos[1] += 1
                    elif s == 4:
                        # Zufällige Bewegung
                        #      [zufälliger x-Wert (-1,0,1) , zufälliger y-Wert (-1,0,1) ]
                        Temp = [random.randrange(3) - 1, random.randrange(3) - 1]
                        # Überprüfung, dass die Summe aus der aktuellen Position und dem Zufallswert im Simulationsfenster liegt.
                        if überprüfeValidität(Wesen.pos[0] + Temp[0],
                                              Wesen.pos[1] + Temp[1]):
                            # Zu der aktuellen x- und y-Postion wird der jeweilige Zufallswert addiert.
                            Wesen.pos[0] += Temp[0]
                            Wesen.pos[1] += Temp[1]

        # Nach jedem Tick wird der anfängliche Wert von 200 um 1 verringert.
        # Deswegen dauert eine Simulation auch länger, je länger die Berechnungen dauern.
        # Somit ist die Länge einer Simulation proportional zur Leistung des PCs, auf dem die Simulation ausgeführt wird.
        Generation[1] -= 1


def main():
    # Deklarierung der Variablen als Global, sodass jedes Objekt und jede Funktion darauf zugreifen kann.
    global WesenListe, Generation, Größe, GenomGröße, PositionsListe, Safezone, Überlebende, GesamtAnzahl
    # Initialisierung Pygames.
    pygame.init()
    # In dieser Liste werden alle Wesen gespeichert.
    WesenListe = []
    # Von jedem Wesen werden 8 Positionen gespeichert, sodass die Bewegung nachverfolgbar ist. (Siehe "Der Schweif hinter den Wesen" in der Dokumentation)
    PositionsListe = [[], [], [], [], [], [], [], []]
    # Alle überlebenden Wesen werden in dieser Liste gespeichert.
    Überlebende = []
    # Eine Generation dauert 200 Ticks, es sei denn, die Wesen bewegen sich vorher nicht mehr.
    # Danach werden die ablaufenden Ticks (Generation[1]) 
    # wieder auf den Standard-Wert 200 (Generation[2]) gesetzt 
    # und die Generationenanzahl (Generation[0]) um 1 erhöht.
    # [Generationenanzahl, Ablaufende Ticks, Standard-Zeitwert für die ablaufenden Ticks]
    Generation = [1, 200, 200]
    # Größe des Simulationsfensters.
    Größe = [100, 100]
    # Anzahl der Wesen.
    GesamtAnzahl = 200
    # Liste, die alle Felder, die die Safezone markieren, beinhaltet.
    Safezone = []
    # Safezone
    SafezoneX = Größe[0] - 1
    while SafezoneX >= 0:
        SafezoneY = Größe[1] - 1
        while SafezoneY >= 0:
            # Über die Intervalle für X und Y lässt sich die Safezone bestimmen.
            # Es wird von 100 bis 0 iteriert und, wenn sich SafezoneX/SafezoneY im Safezone-Bereich befinden, 
            if SafezoneX >= 0 and SafezoneX <= 30 and SafezoneY >= 0 and SafezoneY <= 30:
                # werden deren aktuelle Werte der Safezone-Liste angehängt.
                Safezone.append([SafezoneX, SafezoneY])
            SafezoneY -= 1
        SafezoneX -= 1

    # Die Größe (Anzahl der Genome) des Erbguts wird festgelegt. Je größer das Erbgut, desto komplizierter der Organismus. (Beispiel: Bakterium = 1
    #                                                                                                                                 Mensch = 1000)
    # Wenn die Simulation auf einem etwas älteren PC ausgeführt wird, 
    # sollte die Genomgröße verringert werden.
    GenomGröße = 10

    # Mit den definierten Parametern werden die Wesen generiert.
    generieren()

    # Die Fenstergröße wird festgelegt. (Der Faktor 8 und der Summand 59 fungiert wieder als Anpassung an die Größe des Pygamefensters)
    Fenster = pygame.display.set_mode((Größe[0] * 8 + 59, Größe[1] * 8 + 59))

    # Fenstertitel: 'Survival of the fittest - Wer ist am besten angepasst ?' wird festgelegt.
    pygame.display.set_caption(
        'Survival of the fittest - Wer ist am besten angepasst ?')

    # Während das Programm läuft, gibt es nach jeder Generation eine 5ms Pause, um Komplikationen zwischen den Generationen zu vermeiden.
    # Daraufhin wird das Fenster gerendert, überprüft, ob die Simulation überhaupt noch läuft und dann die Main-Funktion ausgeführt.
    while True:
        pygame.time.delay(5)
        renderFenster(Fenster)
        GenerationsEnde()
        simulationStart()
    pass


if __name__ == "__main__":
    main()
