![github-header-image](https://user-images.githubusercontent.com/111282979/202478536-29589dd2-2e8c-44dd-ba54-c7c463fa43de.png)

<img src="https://user-images.githubusercontent.com/111282979/203019520-8f5bb350-82f7-41cb-a5b9-6865cea33f66.gif" width="650px" height="650px"/>

- [Der Hintergrund](#der-hintergrund)
- [Das Grundprinzip](#das-grundprinzip)
- [Was ist Pygame?](#was-ist-pygame?)

# Der Hintergrund

Wie durch die Chronologie der Blogeinträge bereits erkennbar wurde, war dieses Projekt nicht das erste, an welchem wir gearbeitet haben. Leider scheiterte die Umsetzung als Mobilapp durch die Kosten von 100€ für einen Apple-Developer Account. Nachdem wir zu dieser Erkenntnis gelangen, suchten wir nach einem neuen Projekt.
Einflussreich waren dabei der Biologieunterricht des vergangenen Jahres sowie [Conway's Spiel des Lebens](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens "Conway's Spiel des Lebens").

# Das Grundprinzip

Das Programm stellt eine Evolution dar. Wesen mit unterschiedlichen Genen geben ihr Bestes, um die grünmarkierte Safezone zu erreichen. Wer am Ende der Generation die Zone erreicht hat, gibt seine Gene an die nächste Generation weiter.
Zu Beginn erhalten alle Wesen ein zufälliges Erbgut.
Dieses besteht aus X-Genen, Y-Genen und Z-Genen.
Wie in der menschlichen DNA gibt sind die Gene zweigeteilt. X[1] und X [2] sowie Y[1] und Y[2] nur Z hat lediglich einen Wert. 
Davon abhängig sind die Bewegung jedes einzelnen Wesens und seine Farbe.
Nun gilt: Wessen Gene es in die Safezone schaffen, werden weitergegeben.
Somit werden zunehmend Wesen mit ähnlichen Genen übrig bleiben, die fast alle die Safezone erreichen.

# Was ist Pygame?

Die Simulation lässt sich natürlich komplett über Mathematik und Daten auswerten. Da man sich dadurch jedoch wenig vorstellen kann, wie das Ganze eigentlich aussehen müsste, wird in diesem Projekt [Pygame](https://www.pygame.org/) genutzt, um eine lebhafte Simulation zu ermöglichen.
Pygame ist eine Pythonbibliothek, die zur Spieleprogrammierung genutzt wird.


## Das Wesen

Lila             |Pink            |Grün            |Hautfarbe            |Blau  
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Screenshot (21)](https://user-images.githubusercontent.com/111282979/202292263-010a98a2-c3b9-4c74-9d0a-a9044728c4c3.png)|![Screenshot (22)](https://user-images.githubusercontent.com/111282979/202292396-9ee88ca2-e483-4e44-8270-71874bb1585b.png)|![Screenshot (27)](https://user-images.githubusercontent.com/111282979/202292456-1963d65d-4299-4f87-b920-d56349f8b9d5.png)|![Screenshot (24)](https://user-images.githubusercontent.com/111282979/202292505-d3b0a395-f1c7-42d9-b514-ac72aaa20b56.png)|![Screenshot (25)](https://user-images.githubusercontent.com/111282979/202292567-007dd1f0-c356-492a-a688-cda0d7002c55.png)|

In unserer Simulation gibt es eine festlegbare Anzahl an Wesen.
Ein Wesen hat ein Größe von einem Feld (Kästchen).
Jedes Wesen ist als Objekt definiert und besitzt einen Parameter Genomgröße.
Die [GenomGröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe) beschreibt die Menge der Genome.
Ein [Genom](https://de.wikipedia.org/wiki/Genom) beinhaltet die Gesamtheit der vererbbaren Informationen einer Zelle und ist bei uns ([vgl. Abbildung](https://user-images.githubusercontent.com/111282979/202248021-fbc11b40-15dc-49b3-b351-b211b11420cd.png)) die Gesamtheit der x, y- und z-Gene. Den einzelnen Genen sind verschiedene Werte zugeschrieben, wobei die gesamte Kombination eines Genoms bestimmt, wie sich das Wesen in einer Generation bewegt.
Wie angepasst die Bewegung eines Wesens ist, geht daraus hervor, ob das Wesen bis zum Ende der Generation die [Safezone](#die-safezone) zu erreichen. 
Wenn das Wesen dies tut, dann gibt es seine Gene an die Wesen der nächsten Generation weiter, damit diese bessere Chancen haben, die Safezone zu erreichen.
Daraus ergibt sich, dass die einzige Aufgabe jedes Wesens ist, so viele Generationen wie möglich zu überleben, indem es durch die Bewegung zufällig die Safezone erreicht. 
In dieser Simulation hat das Wesen nicht die Möglichkeit, sich aktiv zu bewegen oder zu verändern. Es ist auf seine Gene angewiesen, die ihm eine Bewegungsart verleihen.
Wenn das Wesen Glück oder Pech hat, kann es auch noch zu einer Mutation seiner Gene kommen, was sich entweder positiv oder negativ auf seine Überlebenschancen auswirkt. 
Die Gene nehmen auch Einfluss auf die Farbe. Diese hat allerdings keine Auswirkung auf die Überlebensrate, so wie es in der Natur mit Warnfarben der Fall ist, da sich die Wesen nicht gegenseitig fressen und kennzeichnet lediglich Wesen mit ähnlichen Genen. 
Die Gesammtanzahl der Wesen bleibt von Generation zu Generation konstant, da sie sich nicht aktiv schaden oder bekämpfen.

# Das Genom

Das Objekt "Genom" beinhaltet drei verschiedenen Gentypen, die auch als Parameter übergeben werden.
Das X-Gen, Y-Gen und Z-Gen. Wie diese Gene initiiert werden (also, wie sie beispielsweise in zwei Werte geteilt werden oder welche Werte ihnen gegeben werden) ist
bis dato nicht festgelegt.

![GenomGrafik](https://user-images.githubusercontent.com/111282979/202248021-fbc11b40-15dc-49b3-b351-b211b11420cd.png)

## Die Mutation

Jedes Wesen besitzt eine einstellbare [GenomGröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe). 
Damit die ganze Genetik noch realistischer ist, können die Gene jedes Genoms nun mit einer Wahrscheinlichkeit von 2% mutieren. Dabei hat jedes einzelne Genom zu Beginn der Runde einen zufälligen Mutationswert, welcher im Intervall [0;15] liegt. Abhängig von dem Mutationswert, bestimmt die Zahl, welches Gen genau mutiert.

Mutationswert|Mutationswert = 0          |Mutationswert = 1          |Mutationswert = [2;4]      |Mutationswert = [5;7]      |Mutationswert =  [8;15]    |      
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
Mutierendes Gen|x0-Gen mutiert             |x1-Gen mutiert             |y0-Gen mutiert             |y1-Gen mutiert             |z-Gen mutiert              |
zugeteilter Wert zum Gen |zufälliger Wert zwischen 0 und 1|zufälliger Wert zwischen 0 und 1|zufälliger Wert zwischen 0 und 7|zufälliger Wert zwischen 0 und 7|zufälliger Wert zwischen 0 und 8|

Wenn der Mutationswert "0" beträgt , mutiert das x0-Gen, bei einem Mutationswert von "1" hingegen das x1-Gen.Wenn der Wert im Intervall [2;4] liegt, dann mutiert das y0-Gen und wenn die Zahl Im Intervall [5;7] liegt das y1-gen. Wennn der Wert sogar im Intervall [8;15] liegen sollte , mutiert das z-Gen. Insgesammt lässt sich abschließend betrachten, dass die Anzahl der Gesammtmutationen propotional zur Genomanzahl ist. Wenn man allerdings jedes Genom einzeln betrachtet, ist hier die Wahrscheinlichkeit konstant, dass ein Genom zu 1/50 also 2% mutiert. Eine Mutation kann sich zwar einserseits positiv auf das Überleben des Wesens auswirken, weil es die Bewegungsart zufällig verändert. Gleichzeitig kann eine Mutation aber auch negative Folgen mit sich bringen, weil alles auf dem Zufall beruht.


![carbon (4)](https://user-images.githubusercontent.com/111282979/202468026-da998a81-9e79-44fb-adc0-f65f6c37acb3.png)

# Der Simulationsbeginn

Sobald die Simulation startet, wird zuerst abgefragt, ob die Generation noch läuft.
Daraufhin wird bei jedem Tick der Generation (von 200 bis 1) durch die Liste der Wesen iteriert und für jedes Wesen ein "stabiler Wert" definiert.
Dazu wird auch eine Variable mit dem Namen "Veränderung" definiert, die die aktuelle Position, den Zeitwert, 
Dieser "stabile Wert" wird im Folgenden dazu genutzt, die "Veränderung" zu speichern.


# Die zufällige Bewegung der Wesen

Die Bewegung jedes Wesens steht in Abhängigkeit zu dessen Genen.
Je nachdem, welches X-, Y-, und Z-Gen vorhanden ist und auf welcher Höhe und Breite sich das Wesen befindet, bewegt sich das Wesen schneller oder langsamer nach oben, unten, links oder rechts.

## Die Veränderung
Da wir versuchen, die Bewegung der Wesen so zufällig, wie möglich zu machen, haben wir uns überlegt, möglichst viele Einflussfaktoren einzubeziehen.
Um einen Wert zu erhalten, der diese Kombination der Einflussfaktoren beinhaltet, haben wir **die Veränderung** eingeführt.
Der Name mag zwar im ersten Moment ein wenig komisch erscheinen, jedoch besagt dieser genau das, wofür die Variable da ist.
Sie beschreibt die Veränderung, die letztendlich an der Position eines Wesens vorgenommen werden soll, sodass daraus durch mehrfaches Wiederholen eine flüssige Bewegung entsteht.
Da diese Faktoren, die einen Einfluss auf die Bewegung nehmen sehr zahlreich sind, werden sie in der folgenden Tabelle veranschaulicht.
Zu Beginn, nachdem der [stabile Wert](#der-stabile-wert) definiert wurde, wird durch alle Genome jedes Wesens iteriert.

```python
for i, Wesen in enumerate(WesenListe):
  stabilerWert = [[0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
  for j, genom in enumerate(Wesen.Gene):
```

Nun werden mehrere Bedingungen ineinander verschachtelt.
Das Ganze beginnt mit einer Hauptbedingung:

```python
if x_gen[0] == 0:
```

![Screenshot (30)](https://user-images.githubusercontent.com/111282979/204501332-41445875-13b4-4159-ac91-ee6d7a3883c1.png)

y0-gen == 0                |y0_gen == 1                |y0_gen == 2                |y0_gen == 3                |y0_gen == 4                |y0_gen == 5
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
Die y-Position des Wesens wird der Veränderung hinzugefügt|Die x-Position des Wesens wird der Veränderung hinzugefügt|Der aktuelle Zeitpunkt (Tick) der Generation wird der Veränderung hinzugefügt|Die Tatsache, dass das Wesen sich in der Safezone befindet wird der Veränderung als Wert hinzugefügt|Ein zufälliger Wert zwischen 0 und 4, multipliziert mit dem z_gen / 8, wird der Veränderung hinzugefügt|Ein zufälliger Wert zwischen 0 und 3, multipliziert mit dem z_gen / 8, wird der Veränderung hinzugefügt|

Nun, da die Veränderung durch alle möglichen Einflüsse verändert wurde, soll diese abgespeichert werden, da sie bei jedem Zeitpunkt wieder neuen Einflüssen ausgesetzt ist. Um die Veränderung folglich statisch und sicher abspeichern zu können, nutzen wir den [stabilen Wert](#der-stabile-wert). An welcher Stelle die Veränderung gespeichert wird, ist abhängig vom jeweiligen Wert des x1-gens (entweder 0 oder 1).
Das x1-gen entscheidet, ob die erste oder zweite Liste für die Speicherung genutzt werden soll. An welcher Stelle genau, ist jedoch abhängig vom 

Wert des x1-Gens           |x1_gen = 1               |x1_gen = 1
:-------------------------:|:-------------------------:|:-------------------------:|
In welcher Liste die Veränderung gespeichert wird| Wird in Liste 1 gespeichert<br>([0, 0, 0, 0])| Wird in Liste 2 gespeichert<br>([0, 0, 0, 0, 0, 0, 0, 0])

An welcher Stelle (Index) die Veränderung in der jeweiligen Liste nun jedoch genau gespeichert wird, ist abhängig von einer Berechnung.


-- Latex Gleichung einfügen
<img src="https://render.githubusercontent.com/render/math?math=\frac{y1_gen}{2 - x1_gen}">

-------


Das y1_gen wird durch (2 - x1-gen) geteilt und das Ergebnis in einen Integer (Ganzzahl) gerundet.
Da das y1_gen einen Wert zwischen 0 und 8 haben kann und das x1_gen entweder 0 oder 1 beträgt, kann sich bei dieser Rechnung jede Ganzzahl zwischen 0 und 8 ergeben. Somit besteht die Möglichkeit, abhängig von den Genen des Wesens, die Veränderung an jeder Stelle der Liste zu speichern.

![carbon (6)](https://user-images.githubusercontent.com/65679099/203022345-ae6ef6a8-d340-4779-b36f-eeff81980d6b.png)

## Der stabile Wert
Eine der elementarsten Datenspeicherungen in unserer Simulation bildet der stabile Wert.
Jedes Wesen besitz einen eigenen stabilen Wert.
Dieser besteht aus einer [verschachtelten Liste](https://github.com/algerr/VocabNow/blob/1dfc29ce07933b6082c18c72e7a229793dc04fcb/sotf.py#L236) mit zwei Listen.

```python
stabilerWert = [[0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
```

Liste                      |Erste Liste                |Zweite Liste
:-------------------------:|:-------------------------:|:-------------------------:|
Werte                      |[0, 0, 0, 0]               |[0, 0, 0, 0, 0, 0, 0, 0]

Die erste Liste besteht aus 4 Werten und die zweite aus 8 Werten.
Doch welche Funktion erfüllt der stabile Wert denn nun eigentlich? 
Die [Veränderung](#die-veränderung) wird im stabilen Wert gespeichert.

## Zufällige Ausführung der Bewegungen

Nun haben wir bei jedem Tick unserer Simulation eine Liste mit zufälligen Werten, die aus den Genen des Wesens berechnet wurden.
Um nun auch wirklich zufällig die Bewegungen auszuführen, erstellen wir eine weitere Liste, genannt: "ZufälligeBewegungen".
Es wird durch die Liste der stabilen Werte iteriert und jeder Wert wird, multipliziert mit einem zufälligen Wert zwischen 0 und 39, der Liste der ZufälligenBewegungen angehängt. 
Nun wird das letzte Mal die Liste der zufälligen Bewegungen enumeriert.
Dabei gibt die Variable *s* den Index des Wertes in der Liste (von 0 bis 7) an und die Variable *Aktion* den Wert an sich.
Damit kein unnötiger Fehler auftritt, wird noch die Bedingung überprüft, dass die Variable *Aktion* größer als 0 ist.
Dazu soll die Bedingung auch nur erfüllt sein, wenn *Aktion* das Maximum aller Werte ist (von ZufälligeBewegungen[0] bis ZufälligeBewegungen[0]).
Nun wird der Index des Maximums der Liste, der in *s* gespeichert ist, entscheidend.
Dieser kann zwischen 0 und 7 liegen, doch, da die Bewegung, bzw. Änderung der Position eines Wesens nur in alle vier Himmelsrichtungen erfolgen kann, haben wir die Indizes 5 bis 7 bisher nicht implementiert. 

Index (s)                  |s = 0                      |s = 1                      |s = 2                      |s = 3                      |s = 4|
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
Änderung der Position      |Ein Feld nach links        |Ein Feld nach rechts       |Ein Feld nach oben         |Ein Feld nach unten        |Zwei zufällige Werte zwischen [-1;1] werden jeweils zur x und y Koordinate addiert|


## Überprüfung der Validität

Da die Simulation, um schöne Ergebnisse mit dennoch komplexen Genen zu erhalten, viele Generationen durchlaufen muss, wäre es ziemlich schade, wenn auf einmal, ein Fehler, bezüglich der Koordinaten eines Wesens, auftreten würde.
Dafür haben wir eine Funktion "überprüfeValidität" mit den Parametern "(x, y)" definiert, die überprüft, dass die Koordinaten jedes Wesens im Simulationsfenster liegen.
Dazu ist es aber auch ungünstig, wenn sich mehrere Wesen auf dem gleichen Feld befinden können, da somit der Konkurrenzkampf darunter leidet.
Infolgedessen, wird noch überprüft, ob die x- und y-Position jedes Wesen mit den übergebenen Werten übereinstimmt.
Sollte das der Fall sein, wird ein False-Statement zurückgegeben, sodass die eingegebenen Werte keine validen Positionen sein können.
Wenn keine Äquivalenz zu den Positionen eines anderen Wesens vorliegt, wird ein True-Statement zurückgegeben und die eingegebenen Werte sind valide Positionen.

![überprüfeValiditätCarbon](https://user-images.githubusercontent.com/65679099/202256158-ccb9bd2e-1091-47c0-8350-b7cf945b668c.png)


# Die Safezone

Die Safezone ist die grün gekennzeichnete Fläche, welche auch das "Zielfeld" markiert, in welchem sich die Wesen bis zum Ende einer Generation befinden sollten, damit sie ihre Gene weitergeben. Die Wesen wissen nicht, wo sich die Safezone genau befindet und sind deshalb auf ihre Bewegungsart angewiesen bzw. müssen hoffen, dass sie durch ihre Bewegungsart die Zone bis zum Ende einer Generation erreichen. Die Wesen, welche es rechzeitig schaffen die Safezone zu erreichen, geben ihre Gene und somit auch ihre Bewegungsart weiter, damit in der nächsten Generation die neu entstandenen Wesen, welche jetzt hauptsächlich die Bewegungsart ihrer Vorfahren übernommen haben, ebenfalls die Safezone erreichen. Dieser Vorgang wiederholt sich immer wieder, wobei gehofft wird, dass irgendwann alle Individuen die Safezone erreichen.
Das ist jedoch unmöglich, da Mutationen immer auftreten können oder manche sich direkt zu Beginn in der Safezone befinden und sich überhaupt nicht bewegen, sodass ihr Überleben durch das Feld, in dem sie erscheinen, abhängt. Die Safezone verändert sich von Generation zu Generation nicht, weil die Weitergabe der erfolgreichen Bewegungsart, keinen Sinn ergibt, wenn sich die Safezone mit jedem Mal ändert. Dann würden sich die Wesen beispielsweise in die komplett falsche Richtung bewegen.


![Screenshot (14)](https://user-images.githubusercontent.com/111282979/202275940-c29e4862-93db-4afe-a4f3-cf434d3aa931.png)

