<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />`Dieses Werk ist lizenziert unter einer`
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">`Creative Commons Namensnennung` - `Nicht kommerziell` - `Keine Bearbeitungen 4.0 International Lizenz`</a>

![SOTF-GIF](https://user-images.githubusercontent.com/65679099/205529978-335f3294-ac76-4dea-ab23-a727b27962aa.gif)

<img src="https://user-images.githubusercontent.com/111282979/203019520-8f5bb350-82f7-41cb-a5b9-6865cea33f66.gif" width="650px" height="650px"/>

# Inhaltsverzeichnis
- [Ausführungsanweisungen](#ausf%C3%BChrungsanweisung)
- [Das Grundprinzip](#das-grundprinzip)
- [Was ist Pygame?](#was-ist-pygame)
- [Das Rendering](#das-rendering)
  - [Der Schweif hinter den Wesen](#der-schweif-hinter-den-wesen)
  - [Der Generationsindikator](#der-generationsindikator)
  - [Die Farbgebung](#die-farbgebung)
- [Das Wesen](#das-wesen)
  - [Die PositionsListe](#die-positionsliste)
- [Das Genom](#das-genom)
  - [Die Mutation](#die-mutation)
- [Die Simulation](#die-simulation)
  - [Das Generieren](#das-generieren)
- [Die zufällige Bewegung der Wesen](#die-zufällige-bewegung-der-wesen)
  - [Die Veränderung](#die-veränderung)
- [Zufällige Ausführung der Bewegungen](#zufällige-ausführung-der-bewegungen)
- [Überprüfung der Validität](#überprüfung-der-validität)
- [Die Safezone](#die-safezone)
  - [Die Initialisierung der Safezone](#die-initialisierung-der-safezone)
  - [Die Vererbung der Gene](#die-vererbung-der-gene)
- [Die Main-Funktion und Initialisierung aller Variablen](#die-main-funktion-und-initialisierung-aller-variablen)
- [Quellenverzeichnis](#quellenverzeichnis)
- [Eigenständigkeitserklärung](#eigenständigkeitserklärung)

# Ausführungsanweisung

Um das Programm zu starten, wird mindestens [Python 3.8](https://www.python.org/downloads) benötigt. 
Sobald Python installiert ist, kann die Installation durch den Befehl `python` in der Eingabeaufforderung überprüft werden. <br>
Wenn die Installation nun also erfolgreich war, muss nur noch die Python-Bibliothek [Pygame](https://www.pygame.org) installiert werden.
Dies ist durch den Python-Packet-Manager `pip` möglich.
Somit muss nur noch der Befehl:
```
python -m pip install pygame
```
in die Eingabeaufforderung eingefügt werden.
Wenn diese Installation erfolgreich abgeschlossen ist, kann das Programm nun fehlerfrei ausgeführt werden.
Dafür muss mit der Eingabeaufforderung in den Ordner, in dem sich die Python-Datei befindet, navigiert werden und daraufhin der Befehl: 
```
python sotf.py
```
ausgeführt werden. <br>
Viel Freude mit dem Programm.

# Der Hintergrund

Wie durch die Chronologie der Blogeinträge bereits erkennbar wurde, war dieses Projekt nicht das erste, an welchem wir gearbeitet haben. Leider scheiterte die Umsetzung als Mobilapp an den Kosten von 100€ für einen Apple-Developer Account. Nachdem wir zu dieser Erkenntnis gelangten, suchten wir nach einem neuen Projekt.
Einflussreich waren dabei der Biologieunterricht des vergangenen Jahres sowie [Conway's Spiel des Lebens](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens "Conway's Spiel des Lebens").

# Das Grundprinzip

Das Programm stellt eine Evolution dar. Wesen mit unterschiedlichen Genen geben ihr Bestes, um die grünmarkierte Safezone zu erreichen. Wer am Ende der Generation die Zone erreicht hat, gibt seine Gene an die nächste Generation weiter.
Zu Beginn erhalten alle Wesen ein zufälliges Erbgut.
Dieses besteht aus X-Genen, Y-Genen und Z-Genen.
Wie in der menschlichen DNA bestehen die Gene aus Basenpaaren. Um diese Paare zu vereinfachen, besteht bei uns das X-Gen aus: `X[1]` und `X[2]`, das Y-Gen aus: `Y[1]` und `Y[2]` und nur das Z-Gen besteht aus einem Wert. 
Davon abhängig sind die Bewegung jedes einzelnen Wesens und seine Farbe.
Nun gilt: Wessen Gene es in die Safezone schaffen, werden weitergegeben.
Somit werden zunehmend Wesen mit ähnlichen Genen übrig bleiben, die fast alle die Safezone erreichen.

# Was ist Pygame?

Pygame ist eine Bibliothek in Python, womit Spiele programmiert werden. Durch die gute Möglichkeit der Visualisierung von Daten in Animationen, wie bei dieser Simulation, lässt sich die Bewegung der Wesen und der Ablauf der Simulation damit gut veranschaulichen.

<details>
<summary>Weiterführende Erklärung</summary>

Die Simulation lässt sich natürlich komplett über Mathematik und Daten auswerten. Da man sich dadurch jedoch wenig vorstellen kann, wie das Ganze eigentlich aussehen müsste, wird in diesem Projekt [Pygame](https://www.pygame.org/) genutzt, um eine lebhafte Simulation zu ermöglichen.
Pygame ist eine Pythonbibliothek, die zur Spieleprogrammierung genutzt wird.

</details>

# Das Rendering

Um die ganze Simulation nun auch wirklich darzustellen, muss das Ganze natürlich gerendert werden. Dafür haben wir die Funktion "renderFenster" definiert, die ein Fenster mit grauem Hintergrund erschafft, das schwarze Feld, worin sich die Simulation abspielt, in der festgelegten Größe einzeichnet und dazu auch die Safezone.
Zum Schluss kommen noch die einzelnen Wesen hinzu und der "Generationszähler", der am oberen rechten Rand die aktuelle Generation indiziert.

<details>
  <summary>Weiterführende Erklärung</summary>

  Zuerst führen wir in der folgenden Tabelle die nützlichen Pygamefunktionen und -objekte auf, die diese Simulation derartig visualisieren, damit beim weiteren Lesen nicht erst die [Pygame-Dokumentation](https://www.pygame.org/docs/) studiert werden muss. Es sind in der Tabelle lediglich die Parameter der Funktionen angegeben, die auch im Projekt benutzt werden.

  Pygamefunktion/-objekt     |Erklärung                  |
  :-------------------------:|:-------------------------:|
  init()                     |Alle Pygame-Module werden initialisiert und die Programmierung mit Pygame kann beginnen. Diese Funktion ist grundlegend und in unserer Main-Funktion an erster Stelle nach der Deklaration der globalen Variablen zu finden. In diesem Projekt nutzen wir keine Parameter für diese Funktion.|
  Surface.fill()             |Eine Oberfläche, in unserem Fall ein Fenster, wird mit einer Farbe gefüllt. Benötigte Parameter: (Die RGB-Werte).|
  draw.rect()                |Ein Rechteck mit beliebiger Größe und Farbe kann gezeichnet werden. Diese Funktion wird in diesem Projekt für das Rendering jeder viereckigen Form genutzt-vom Wesen bis zum schwarzen Hintergrund. Benötigte Parameter: (Die Oberfläche, die RGB-Werte, (der Abstand vom linken Rand, der Abstand vom oberen Rand, die Breite des Rechtecks, die Höhe des Rechtecks)|
  font.Font()                |Es wird ein neues Objekt erstellt. Die Schriftart und Größe können festgelegt werden. Benötigte Parameter: (Schriftart, Größe(Höhe der Schrift in Pixeln))|
  font.Font.render()         |Ein Text wird auf einer neu erzeugten Oberfläche gerendert. Benötigte Parameter: (Der Text, Anti-Aliasing, Farbe des Textes)|
  Surface.blit()             |Eine Oberfläche wird auf eine andere "draufgelegt". Benötigte Paramter: (Neue Oberfläche, Untergrund-Oberfläche|
  display.update()           |Ein gewisser Teil des Pygamefensters kann neu geladen werden. Wenn kein Parameter übergeben wird, wird das gesamte Fenster bzw. die gesamte Oberfläche neu geladen. (In diesem Projekt wird pygame.display.update() ohne Parameter aufgerufen.)|
  display.set_mode()         |Ein Fenster kann mit dieser Funktion initialisiert werden. Benötigte Parameter: (Breite, Höhe)|
  display.set_caption()      |Der Fenstertitel kann mit dieser Funktion festgelegt werden. Benötigte Parameter: (Fenstertitel (Beispiel: "Survival of the fittest - Wer ist am besten angepasst?)|

  Die Funktion, in der das gesamte Rendering erfolgt "renderFenster" besitzt einen Parameter "Fenster". Dieser bildet die grundlegende Oberfläche des Pygamefensters.
  Zuerst wird mit
  ```python
  Fenster.fill((50,50,50))
  ```
  die gesamte Oberfläche grau eingefärbt. Daraufhin wird ein Quadrat mit 
  ```python
  pygame.draw.rect(Fenster, (0,0,0), (29, 29, Größe[0] * 8 + 1, Größe[1] * 8 + 1))
  ```
  auf diese graue Oberfläche gezeichnet. In diesem schwarzen Quadrat spielt sich die gesamte Simulation ab.
  In der draw.rect() Funktion wird die Oberfläche "Fenster", die Farbe (0,0,0) (schwarz) und der Abstand vom linken sowie oberen Rand und die Größe des Quadrats übergeben. Die Größe haben wir standardmäßig, damit die nachfolgenden Rechnungen einfacher sind, auf 100 gesetzt. Damit das Ganze an das Fenster angepasst ist, wird der Faktor 8 genutzt und zum Schluss noch 1 dazuaddiert. Diese Multiplikationen und Additionen werden häufiger im Quelltext auftreten, da alles genau an die Fenstergröße angepasst wird. Nach dem schwarzen Quadrat wird nun auch schon die [Safezone](#die-safezone) gezeichnet. Hierbei, damit die Rasterstruktur der Simulation beibehalten wird, wird die Liste "Safezone", in der jedes Feld mit x- und y-Koordinate gespeichert ist, enumeriert und jedes Feld als einzelnes kleines Quadrat gezeichnet.
  ```python
  pygame.draw.rect(Fenster, (0, 100, 0), (30 + zielpunkt_der_safezone[0] * 8, 30 + zielpunkt_der_safezone[1] * 8, 7, 7))
  ```
  Die grüne Farbe wird durch die RGB-Werte (0, 100, 0) festgelegt. Hier ist bereits das erste Beispiel für die Multiplikation und Addition, die benötigt wird, um die Größe an das Fenster anzupassen. Um die Felder mit ein wenig Abstand zueinander zu zeichnen, wird jede x- und y-Koordinate des Feldes mit 8 multipliziert und mit 30 addiert. Die Größe eines Feldes beträgt (7,7), somit muss bei draw.rect() für die Breite und Höhe der Wert 7 eingegeben werden.

  ## Der Schweif hinter den Wesen

  Um die Bewegung jedes Wesens erkennbar zu machen, wird nicht einfach nur das farbige Feld verschoben, sondern jedem Wesen wird auch ein kleiner werdender Schweif "angehängt". Dieser hat eine Länge von bis zu 8 Feldern.<br>
  Die [PositionsListe](#die-positionsliste) ist eine verschachtelte Liste mit 8 inneren Listen. In diesen Listen werden die vorherigen Positionen der Wesen gespeichert. Durch die Speicherung der Positionen ist es möglich, auch auf diesen vorherigen Positionen mit draw.rect() ein Rechteck zu zeichnen. Je weiter die Position von der aktuellen entfernt ist, desto dunkler wird sie gefärbt. So lässt sich, wie bei einer Sternschnuppe, die Bewegung der Wesen nachverfolgen.
  Die PositionsListe wird mit *PositionsListenWerte* enumeriert und daraufhin werden die *PositionsListenWerte* mit der Variable *altePosition* enumeriert.<br>
  Dadurch ist es möglich, die gespeicherten alten Positionen aus der PositionsListe der Reihe nach zu färben. Da die PositionsListe mit den ältesten Positionen beginnt und mit den aktuellsten aufhört, wird mit jedem Durchlaufen des for-Loops, die Farbe des Feldes erhöht. Somit werden, je näher man der aktuellen Position des Wesens kommt, die Felder der ehemaligen Positionen heller gefärbt.
  ```python
  for i, PositionsListenWerte in enumerate(PositionsListe):
    # Nun wird durch die Positionsdaten (also PositionsListenWerte) iteriert und das Ganze in "altePosition" gespeichert
    for j, altePosition in enumerate(PositionsListenWerte):
    # Je nachdem, welchen Index die Position hat, wird sie dunkler/heller gefärbt
    # Der erste gespeicherte Wert (die älteste Position) wird mit i=0 bezeichnet
    # Also beträgt der Farbwert (5 + 0*10)
    # Somit ist der RGB Wert ((5+0*10),(5+0*10),(5+0*10)) also (5,5,5)
    # Je neuer der gespeicherte, alte Wert ist, also, je näher er an der aktuellen Position liegt,
    # desto heller wird er.
    # Somit wird der aktuellste gespeicherte Wert (nach dem aktuellen) mit i = 7 bezeichnet
    # Also ist der RGB Wert ((5+7*10),(5+7*10),(5+7*10)) also (75,75,75), welcher definitiv heller ist als (5,5,5)
    # Die altePosition wird mit dem Faktor 8 und dem Summanden 30 an die Größe des Fensters angepasst
    # Und anschließend wird jede altePosition in ihrer Farbe gezeichnet
      pygame.draw.rect(Fenster, (5 + i * 10, 5 + i * 10, 5 + i * 10), (30 + altePosition[0] * 8, 30 + altePosition[1] * 8, 7, 7))
  ```

  ## Der Generationsindikator

  Da sich in der Simulation mit jeder Generation die Wesen weiterentwicklen und man sich natürlich fragt, wie lange es denn eigentlich dauert, bis die meisten Wesen die richtigen Gene besitzen, um die Safezone jedes Mal zu erreichen, ist ein Indikator, der die aktuelle Generation anzeigt, von Vorteil. Hierbei wird ein neues Schriftobjekt mit font.Font() initiiert, genannt "generationsIndikator". Diesem wird keine besondere Schriftart zugeschrieben, jedoch eine Schriftgröße von 30 Pixeln. 
  ```python
  generationsIndikator = pygame.font.Font(None, 30)
  ```
  <br>
  Um den Text zu rendern, wird eine neue Oberfläche "generationsRendering" definiert, die das Schriftobjekt rendert. 

  ```python
  generationsRendering = generationsIndikator.render("Generation:" + str(Generation[0]), True, (255, 120, 0))
  # Der Text wird oben rechts über das schwarze Quadrat geschrieben
  Fenster.blit(generationsRendering, generationsRendering.get_rect(center=(Größe[0] * 8 + 59 - 90, 20)))
  ```

  Der Text beinhaltet "Generation: " und die aktuelle Generationenanzahl. Anti-Aliasing ist aktiviert, da dies den Text glättet, indem unerwünschte Pixel, die durch das Pixelraster entstehen, vermindert werden. Die Farbe des Textes ist ein kräftiges Orange (255, 120, 0).
  Nun wird zum Schluss noch die Oberfläche mit dem Generationsindikator auf die normale Oberfläche des Fensters "draufgelegt".
  Die Position des Textes wird festgelegt, wobei wieder der Faktor 8 für die Anpassung der Größe an die des Pygamefensters auftaucht.
  Zum Schluss wird das gesamte Pygamefenster aktualisiert und alles neu gerendert.
  Dieser Vorgang geschieht bei jedem Zeitwert (Tick) der Generation.

  ## Die Farbgebung

  Die Wesen in unserer Simulation sollen, wie auch die Menschen oder andere Lebewesen, individuell sein. Um nicht jedem Wesen eine zufällige Farbe zu geben, ist der RGB-Wert der Farbe in die drei Bestandteile: "Rot, Grün, Blau" aufgeteilt. Je nachdem, welche Gene das Wesen besitzt, wird sich die Farbe verändern. Die Standardfarbe für ein Wesen mit keinerlei besonderen Genen, die Einfluss auf die Farbe nehmen, ist grau (125, 125, 125 (R,G,B,)). Wesen mit ähnlichen Genen erkennt man an der ähnlichen Farbgebung. Die Wahrscheinlichkeit, dass sie sich infolgedessen auch gleich verhalten/bewegen, ist höher, je ähnlicher die Farben sind.

  <details>
    <summary>Erklärung</summary>

Alles ist ausgehend von den Werten der Standardfarbe grau (125, 125, 125). Je nach Kombination der Gene wird ein Wert mit dem Standardwert summiert oder davon subtrahiert. Um die Wesen auch visuell bezüglich "guter, angepasster Gene" unterscheiden zu können, wird die Anzahl der funktionalen Genome genutzt. Ein Genom gilt als funktional, wenn das x1_gen den Wert 1 besitzt, denn dadurch nimmt dieses Genom einen Einfluss auf die Bewegung des Wesens.<br> (Nur zur Erinnerung: das x1_gen benötigt den Wert 1, um die Veränderung im stabilen Wert zu speichern.)<br> Die Anzahl dieser funktionalen Genome wird folglich durch Enumeration überprüft.

Genkombination|x1_gen = 1 und y1_gen = 0  |x1_gen = 1 und y1_gen = 1  |x1_gen = 1 und y1_gen = 2  |x1_gen = 1 und y1_gen = 3  |x1_gen = 1 und y1_gen = 4  |
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
Veränderung der roten Farbe|Wert wird addiert          |Wert wird subtrahiert      |
Veränderung der grünen Farbe|Wert bleibt gleich         |Wert bleibt gleich         |Wert wird addiert          |Wert wird subtrahiert      |
Veränderung der blauen Farbe|Wert bleibt gleich         |Wert bleibt gleich         |Wert bleibt gleich         |Wert bleibt gleich         |Wert wird addiert |

Nach Feinjustierung hat sich für die Berechnung des zu *addierenden Wertes* ergeben, dass<br> das Minimum aus (254 - *dem Farbwert*) und dem Integer aus ((40 + z_gen * 60) * 2 / Anzahl der funktionellen Gene) <br>**für jegliche Genomgrößen funktioniert**.

Für den zu *subtrahierenden Wert* hat sich ergeben, dass<br> das Minimum aus dem *Farbwert* und dem Integer aus ((40 + z_gen * 60) * 2 / Anzahl der funktionellen Genome) <br>**für jegliche Genomgrößen funktioniert**.

Hierbei ist erkennbar, dass dadurch, dass durch die Anzahl der funktionellen Genome dividiert wird, der Integer kleiner wird, je mehr funktionelle Genome vorhanden sind. Deshalb wird die Wahrscheinlichkeit, dass der Integer kleiner als die Farbe selbst ist, größer. Somit ist der Integer das Minimum der beiden Werte und wird somit vom bisherigen *Farbwert* abgezogen. Deshalb sind Wesen mit vielen funktionellen Genomen, die ausgeprägtere Bewegungen haben, heller gefärbt und diese mit wenigeren funktionellen Genomen, die potentiell auch weniger ausgeprägte Bewegungen besitzen, dunkler gefärbt.

Beim dritten Farbwert (Blau) wird eine Kombination des Additions-/Subtraktionsverfahrens der vorherigen Farben verwendet. 
Durch das Maximum aus dem *negativen Farbwert* und dem<br> Minimum aus ((254 - dem Farbwert) und (80 + z_gen * 60) / Anzahl der funktionellen Genome), kann gewährleistet werden, dass **jegliche Genomgrößen funktionieren**.
Sollte das Minimum geringer als der *Farbwert* mit negativem Vorzeichen sein, wird ein Fehler umgangen, da der *negative Farbwert* dann das Maximum bildet.
Somit ergibt sich mindestens ein *Farbwert* von 0, wenn der *Farbwert* mit dem *negativen Farbwert* addiert wird.

  </details>

  So lassen sich die Wesen nach Anzahl der funktionellen Genome und Kombination von Genen einfärben.

  Das Färben an sich geschieht letztendlich durch das [Rendering](#das-rendering).

</details>
  
# Das Wesen

Lila             |Pink            |Grün            |Hautfarbe            |Blau  
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Screenshot (21)](https://user-images.githubusercontent.com/111282979/202292263-010a98a2-c3b9-4c74-9d0a-a9044728c4c3.png)|![Screenshot (22)](https://user-images.githubusercontent.com/111282979/202292396-9ee88ca2-e483-4e44-8270-71874bb1585b.png)|![Screenshot (27)](https://user-images.githubusercontent.com/111282979/202292456-1963d65d-4299-4f87-b920-d56349f8b9d5.png)|![202292505-d3b0a395-f1c7-42d9-b514-ac72aaa20b56 (1)](https://user-images.githubusercontent.com/65679099/205465711-c0301c56-8532-4d07-b3cc-5b5cad1e8c33.png)|![Screenshot (25)](https://user-images.githubusercontent.com/111282979/202292567-007dd1f0-c356-492a-a688-cda0d7002c55.png)|

In der Simulation gibt es eine festlegbare Anzahl an Wesen.
Ein Wesen besitzt die Größe eines Feldes.
Jedes Wesen ist als Objekt definiert und besitzt einen Parameter, die Genomgröße.
Die [GenomGröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe) beschreibt die Menge der Genome.
Ein [Genom](https://de.wikipedia.org/wiki/Genom) beinhaltet die Gesamtheit der vererbbaren Informationen einer Zelle und ist bei uns ([vgl. Abbildung](https://user-images.githubusercontent.com/111282979/202248021-fbc11b40-15dc-49b3-b351-b211b11420cd.png)) die Gesamtheit der x-, y- und z-Gene. Den einzelnen Genen sind verschiedene Werte zugeschrieben, wobei die gesamte Kombination eines Genoms bestimmt, wie sich das Wesen in einer Generation bewegt.
Wie angepasst die Bewegung eines Wesens ist, geht daraus hervor, ob das Wesen bis zum Ende der Generation die [Safezone](#die-safezone) erreicht. 
Wenn das Wesen dies tut, gibt es seine Gene an die Wesen der nächsten Generation weiter, damit diese bessere Chancen haben, die Safezone zu erreichen.
Daraus ergibt sich, dass die einzige Aufgabe jedes Wesens ist, so viele Generationen wie möglich zu überleben, indem es durch die Bewegung zufällig die Safezone erreicht. 
In dieser Simulation hat das Wesen nicht die Möglichkeit, sich aktiv zu bewegen oder zu verändern. Es ist auf seine Gene angewiesen, die ihm eine Bewegungsart verleihen.
Wenn das Wesen Glück oder Pech hat, kann es auch noch zu einer Mutation seiner Gene kommen, was sich entweder positiv oder negativ auf seine Überlebenschancen auswirkt. 
Die Gene nehmen auch Einfluss auf die Farbe. Diese hat allerdings keine Auswirkung auf die Überlebensrate, so wie es in der Natur mit Warnfarben der Fall ist, da sich die Wesen nicht gegenseitig fressen und kennzeichnet lediglich Wesen mit ähnlichen Genen. 
Die Gesamtanzahl der Wesen bleibt von Generation zu Generation konstant, da sie sich nicht aktiv schaden oder bekämpfen.

## Die PositionsListe

Um die Bewegung der Wesen nachverfolgen zu können, werden die vorherigen 8 Positionen gespeichert und unterschiedlich [gefärbt](#der-schweif-hinter-den-wesen).
Um die PositionsListe jedoch immer zu aktualisieren, bedient man sich eines while-Loops. Da die PositionsListe 8 innere Listen besitzt, definieren wir einen *LoopZähler* mit dem Wert 7. <br>
Solange der LoopZähler also größer 0 ist, wird der Wert der PositionsListe an der Stelle (7 - LoopZähler) mit dem Wert der PositionsListe an der Stelle (8 - LoopZähler) ersetzt. Daraufhin wird der LoopZähler um 1 verringert.
Somit rückt jede Position immer eine Liste weiter nach vorne.
Anschließend wird die gespeicherte Position an letzter Stelle (8. Liste der PositionsListe) gelöscht, sodass Platz für eine neue vorhanden ist.
```python
while LoopZähler > 0:
  PositionsListe[7 - LoopZähler] = PositionsListe[8 - LoopZähler]
  LoopZähler -= 1
PositionsListe[7] = []
```
Mit diesem Vorgehen kann die Position des Wesens jedes Mal auf's Neue gespeichert werden und jede bisherige Position rückt in der PositionsListe um eine Liste weiter nach vorne. Die PositionsListe ist zudem rückwärts zu lesen, da die neue Position eines Wesens, nachdem das Wesen auf der Oberfläche gerendert wurde, an letzter Stelle der PositionsListe gespeichert wird.
```python
pygame.draw.rect(Fenster, (int(farbe[0]), int(farbe[1]), int(farbe[2])), (30 + Wesen.pos[0] * 8, 30 + Wesen.pos[1] * 8, 7, 7))
# Die Positionen der Wesen werden gespeichert
PositionsListe[7].append([Wesen.pos[0], Wesen.pos[1]])
```

# Das Genom

Das Objekt `Genom` beinhaltet drei verschiedene Gentypen, die auch als Parameter übergeben werden - 
das `X-Gen`, `Y-Gen` und `Z-Gen`. Wie diese Gene initiiert werden (wie sie beispielsweise in zwei Werte geteilt werden oder welche Werte ihnen gegeben werden) ist
bis dato nicht festgelegt.
Somit könnte zur Zeit noch alles darin gespeichert werden, denn, was konkret gespeichert wird, wird erst später festgelegt.

![GenomGrafik](https://user-images.githubusercontent.com/111282979/202248021-fbc11b40-15dc-49b3-b351-b211b11420cd.png)

## Die Mutation

Jedes Wesen besitzt eine einstellbare [Genomgröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe). 
Damit die ganze Genetik noch realistischer ist, können die Gene jedes Genoms nun mit einer Wahrscheinlichkeit von 2% mutieren. Dabei hat jedes einzelne Genom zu Beginn der Runde einen zufälligen Mutationswert, welcher im Intervall [0;15] liegt. Abhängig von dem Mutationswert bestimmt die Zahl, welches Gen genau mutiert.

<details>
  <summary>Erklärung</summary>
  
  Mutationswert|Mutationswert = 0          |Mutationswert = 1          |Mutationswert = [2;4]      |Mutationswert = [5;7]      |Mutationswert =  [8;15]    |      
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
Mutierendes Gen|x0-Gen mutiert             |x1-Gen mutiert             |y0-Gen mutiert             |y1-Gen mutiert             |z-Gen mutiert              |
zugeteilter Wert zum Gen |zufälliger Wert zwischen 0 und 1|zufälliger Wert zwischen 0 und 1|zufälliger Wert zwischen 0 und 7|zufälliger Wert zwischen 0 und 7|zufälliger Wert zwischen 0 und 8|

Wenn der Mutationswert `0` beträgt , mutiert das x0-Gen. Bei einem Mutationswert von `1` hingegen das x1-Gen. Wenn der Wert im Intervall `[2;4]` liegt, dann mutiert das y0-Gen und wenn die Zahl Im Intervall `[5;7]` liegt das y1-Gen. Wenn der Wert sogar im Intervall `[8;15]` liegen sollte , mutiert das z-Gen. Insgesamt lässt sich abschließend sagen, dass die Anzahl der Gesamtmutationen proportional zur Genomanzahl ist. Wenn man allerdings jedes Genom einzeln betrachtet, ist hier die Wahrscheinlichkeit konstant, dass ein Genom zu 2% mutiert. <br>
Eine Mutation kann sich zwar einerseits positiv auf das Überleben des Wesens auswirken, weil es die Bewegungsart zufällig verändert. Gleichzeitig kann eine Mutation aber auch negative Folgen mit sich bringen, weil alles auf dem Zufall beruht.
  
</details>

![carbon (14)](https://user-images.githubusercontent.com/65679099/207897194-721fcab6-37ac-47e6-a606-86da577570b4.png)

# Die Simulation

Sobald die Simulation startet, wird zuerst abgefragt, ob die Generation noch läuft.
Daraufhin wird bei jedem Tick der Generation (von 200 bis 1) durch die Liste der Wesen iteriert und für jedes Wesen ein `stabiler Wert` definiert.
Dazu wird auch eine Variable mit dem Namen `Veränderung` definiert, die die aktuelle Position und weitere momentane Eigenschaften des Wesens beschreibt.
Dieser "stabile Wert" wird im Folgenden dazu genutzt, die `Veränderung` zu speichern.

## Das Generieren

Damit die Simulation beginnen kann, werden die Hauptakteure des Ganzen benötigt - die Wesen.
Dafür haben wir die Funktion "generieren" definiert, welche die festlegbare Gesamtanzahl an Wesen in einer temporären Variable speichert und daraufhin solange Wesen mit der festgelegten Genomgröße erschafft, bis der temporäre Wert 0 beträgt. Nach jedem erschaffenen Wesen, wird der temporäre Wert um 1 verringert.

```python
def generieren():
    Temp = GesamtAnzahl
    # Solange der temporäre Wert größer 0 ist, werden Wesen mit der festgelegten Genomgröße erschaffen
    while Temp > 0:
        WesenListe.append(Wesen(GenomGröße))
        Temp -= 1
```

# Die zufällige Bewegung der Wesen

Die Bewegung jedes Wesens steht in Abhängigkeit zu dessen Genen.
Je nachdem, welches X-, Y-, und Z-Gen vorhanden ist und auf welcher Höhe und Breite sich das Wesen befindet, bewegt sich das Wesen schneller oder langsamer nach oben, unten, links oder rechts.

## Die Veränderung
Da wir versuchen, die Bewegung der Wesen so zufällig wie möglich zu gestalten, haben wir uns überlegt, möglichst viele Einflussfaktoren einzubeziehen.
Um einen Wert zu erhalten, der diese Kombination der Einflussfaktoren beinhaltet, haben wir *die Veränderung* eingeführt.
Der Name mag zwar im ersten Moment ein wenig besonders erscheinen, jedoch besagt dieser genau das, wofür die Variable da ist.
Sie beschreibt die Veränderung, die letztendlich an der Position eines Wesens vorgenommen werden soll, sodass daraus durch mehrfaches Wiederholen eine flüssige und zufällige Bewegung entsteht.
Da diese Faktoren, die einen Einfluss auf die Bewegung nehmen, sehr zahlreich sind, werden sie in der folgenden Tabelle veranschaulicht. <br>
Zu Beginn, nachdem der [stabile Wert](#der-stabile-wert) initialisiert wurde, werden die Genome jedes Wesens enumeriert.

```python
for i, Wesen in enumerate(WesenListe):
  stabilerWert = [0, 0, 0, 0, 0, 0, 0, 0]
  for j, genom in enumerate(Wesen.Gene):
```

Nun steht alles in Abhängigkeit zu einer Hauptbedingung:

```python
if x_gen[0] == 0:
```

**Das x0_gen muss den Wert 0 haben.**

![Screenshot (30)](https://user-images.githubusercontent.com/111282979/204501332-41445875-13b4-4159-ac91-ee6d7a3883c1.png)

y0-Gen == 0                |y0_Gen == 1                |y0_Gen == 2                |y0_Gen == 3                |y0_Gen == 4                |y0_gen == 5
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
Die y-Position(Höhe) des Wesens wird der Veränderung hinzugefügt|Die x-Position(Breite) des Wesens wird der Veränderung hinzugefügt|Der aktuelle Zeitpunkt (Tick) der Generation wird der Veränderung hinzugefügt|Die Tatsache, dass das Wesen sich in der Safezone befindet wird der Veränderung als Wert(z_gen / 2) hinzugefügt|Ein zufälliger Wert zwischen 0 und 4, multipliziert mit dem (z_gen / 8), wird der Veränderung hinzugefügt|Ein zufälliger Wert zwischen 0 und 3, multipliziert mit dem (z_gen / 8), wird der Veränderung hinzugefügt|

Nun, da die Veränderung durch alle möglichen Einflüsse editiert wurde, soll diese nun abgespeichert werden, da sie, bzw. das Wesen, bei jedem Zeitpunkt wieder neuen Einflüssen ausgesetzt ist. Um die Veränderung folglich statisch und sicher abspeichern zu können, nutzen wir den [stabilen Wert](#der-stabile-wert). An welcher Stelle die Veränderung gespeichert wird, ist abhängig vom jeweiligen Wert des x1-Gens (entweder 0 oder 1).
Das x1-Gen entscheidet, ob die Veränderung gespeichert wird oder nicht - an welcher Stelle der Liste genau, ist jedoch abhängig vom Wert des x1-Gens.

Wert des x1-Gens           |x1_Gen = 0               |x1_Gen = 1
:-------------------------:|:-------------------------:|:-------------------------:|
Wie mit der Veränderung verfahren wird| Die Veränderung wird nicht gespeichert| Die Veränderung wird in der Liste gespeichert|

An welcher Stelle (Index) die Veränderung in der jeweiligen Liste nun jedoch genau gespeichert wird, soll jedoch nun auch durch das y- und z-Gen beeinflusst werden.

Das y1_Gen wird durch (2 - x1-Gen) geteilt und das Ergebnis in einen Integer (Ganzzahl) gerundet.
Da das y1_Gen einen Wert zwischen 0 und 8 haben kann und das x1_Gen entweder 0 oder 1 beträgt, kann sich bei dieser Rechnung jede Ganzzahl zwischen 0 und 8 ergeben. Somit besteht die Möglichkeit, abhängig von den Genen des Wesens, die Veränderung an jeder Stelle der Liste zu speichern.

![carbon (6)](https://user-images.githubusercontent.com/65679099/203022345-ae6ef6a8-d340-4779-b36f-eeff81980d6b.png)

## Der stabile Wert
Eine der elementarsten Datenspeicherungen in unserer Simulation bildet der stabile Wert.
Jedes Wesen besitzt einen eigenen stabilen Wert.

```python
stabilerWert = [0, 0, 0, 0, 0, 0, 0, 0]
```

Der stabile Wert besteht aus einer Liste mit 8 einzelnen Werten.

Doch welche Funktion erfüllt der stabile Wert denn nun eigentlich? <br>
Der stabile Wert ist für die Simulation von elementarer Bedeutung, denn er speichert die einzelnen [Veränderungen](#die-veränderung) jedes Wesens, die für die Bewegung genutzt werden.

## Zufällige Ausführung der Bewegungen

Nun haben wir bei jedem Zeitwert (Tick) unserer Simulation eine Liste mit Werten, die aus der Kombination der Gene des Wesens berechnet wurden.
Um die Bewegungen nun auch wirklich zufällig auszuführen, initialisieren wir eine weitere leere Liste, genannt: *ZufälligeBewegungen*.
Die Liste des stabilen Wertes wird nun enumeriert und jeder Wert wird, multipliziert mit einem zufälligen Wert zwischen 0 und 39, der Liste der *ZufälligenBewegungen* angehängt. 
Nun wird das letzte Mal die Liste der *ZufälligenBewegungen* enumeriert.
Dabei gibt die Variable *s* den Index des Wertes in der Liste (von 0 bis 7) und die Variable *Aktion* den Wert an sich an.
Damit kein unnötiger Fehler auftritt, wird noch die Bedingung überprüft, dass die Variable *Aktion* größer 0 ist.
Dazu soll die Bedingung auch nur erfüllt sein, wenn *Aktion* das Maximum aller Werte ist (von ZufälligeBewegungen[0] bis ZufälligeBewegungen[7]).
Nun ist der Index des Maximums der Liste, der in *s* gespeichert ist, von großer Bedeutung.
Dieser kann zwischen 0 und 7 liegen. Da die Bewegung, bzw. Änderung der Position eines Wesens nur in alle vier Himmelsrichtungen erfolgen kann, sind die Indizes 5 bis 7 bisher nicht implementiert. Wenn dafür aber eine gute Idee vorhanden sist, können diese mit Leichtigkeit umgesetzt werden.

Index (s)                  |s = 0                      |s = 1                      |s = 2                      |s = 3                      |s = 4|
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
Änderung der Position      |Ein Feld nach links        |Ein Feld nach rechts       |Ein Feld nach oben         |Ein Feld nach unten        |Zwei zufällige Werte zwischen [-1;1] werden jeweils zur x und y Koordinate hinzuaddiert|


## Überprüfung der Validität

Da die Simulation, um schöne Ergebnisse mit dennoch komplexen Genen zu erhalten, viele Generationen durchlaufen muss, wäre es ziemlich schade, wenn auf einmal ein Fehler bezüglich der Koordinaten eines Wesens oder der Felder der Safezone auftreten würde.
Dafür haben wir eine Funktion `überprüfeValidität` mit den Parametern "(x und y)" definiert, die überprüft, dass die eingegebenen Parameter gültigen Koordinaten im Simulationsfenster entsprechen.
Infolgedessen ist es sehr ungünstig, wenn sich mehrere Wesen auf ein und demselben Feld befinden können, da die Konkurrenz darunter leidet.
Deshalb wird dazu auch noch überprüft, ob die x- und y-Positionen irgendeines Wesens mit den übergebenen Parametern übereinstimmt.
Sollte das der Fall sein, wird ein False-Statement zurückgegeben, das die eingegebenen Werte als invalide Positionen deklariert.
Wenn keine Kongruenz zu den Positionen eines anderen Wesens vorliegt, wird ein True-Statement zurückgegeben und die eingegebenen Werte sind valide Positionen.

![überprüfeValiditätCarbon](https://user-images.githubusercontent.com/65679099/202256158-ccb9bd2e-1091-47c0-8350-b7cf945b668c.png)

# Die Safezone

Die Safezone ist die grün gekennzeichnete Fläche, welche auch das "Zielfeld" markiert, in welchem sich die Wesen bis zum [Ende einer Generation](#nach-dem-ende-der-generation) befinden sollten, damit sie ihre Gene vererben.<br> Die Wesen wissen nicht, wo sich die Safezone genau befindet und sind deshalb auf ihre Bewegungsart und somit auf ihre Gene angewiesen bzw. müssen hoffen, dass sie durch ihre Bewegung die Zone bis zum Ende einer Generation erreichen.<br>
Die Wesen, welche es rechtzeitig schaffen die Safezone zu erreichen, vererben ihre Gene und somit auch ihre Bewegungsart weiter, damit in der nächsten Generation die neu entstandenen Wesen, welche jetzt hauptsächlich die Bewegungsart ihrer Vorfahren übernommen haben, ebenfalls die Safezone erreichen. Dieser Vorgang wiederholt sich immer wieder, wobei gehofft wird, dass irgendwann alle Wesen die Safezone erreichen.
Das ist jedoch unmöglich, da jederzeit Mutationen auftreten können oder manche Wesen sich direkt zu Beginn in der Safezone befinden und sich überhaupt nicht bewegen, sodass ihr Überleben vom Feld, in dem sie erscheinen, abhängig ist. Die Safezone verändert sich von Generation zu Generation nicht, weil die Weitergabe der angepassten Gene, die eine erfolgreiche Bewegungsart bewirken, keinen Sinn ergibt, wenn sich die Safezone mit jedem Mal ändert. Dann müssten sich die Gene der Wesen jedes Mal verändern, was bezüglich des Vererbungsprinzips jedoch nicht mit solcher Präzision möglich ist, dass ein Wesen jede Safezone mit hundertprozentiger Sicherheit erreicht.

![Screenshot (14)](https://user-images.githubusercontent.com/111282979/202275940-c29e4862-93db-4afe-a4f3-cf434d3aa931.png)

## Die Initialisierung der Safezone

Die Initialisierung, bzw. Berechnung der Safezone erfolgt durch einzelne Felder, deren Koordinaten in der Liste `Safezone` gespeichert werden. 
Durch die Variablen `SafezoneX` und `SafezoneY` lässt sich die Safezone beliebig in Breite und Höhe begrenzen.
`SafezoneX` und `SafezoneY` entsprechen zu Beginn der (Größe des Simulationsbereiches - 1).
Nun lassen sich Intervalle festlegen, in denen sich die Safezone befinden soll.
Daraufhin werden die Variablen iterativ um 1 verringert und wenn sie sich im festgelegten Intervall befinden, werden die Werte als x- und y-Koordinaten der "Safezone" Liste angehängt.

```python
Safezone = []
SafezoneX = Größe[0] - 1
while SafezoneX >= 0:
  SafezoneY = Größe[1] - 1
  while SafezoneY >= 0:
    # Über die Intervalle für X und Y lässt sich die Safezone bestimmen
    # Es wird von 100 bis 0 iteriert und, wenn sich SafezoneX/SafezoneY im Safezone-Bereich befinden, werden diese der Safezone Liste angehängt
    if SafezoneX >= 0 and SafezoneX <= 30 and SafezoneY >= 0 and SafezoneY <= 30:
      # Die Safezone Pixel werden festgehalten
      Safezone.append([SafezoneX, SafezoneY])
    SafezoneY -= 1
  SafezoneX -= 1
```

# Nach dem Ende der Generation

Zuerst wird überprüft, ob das Pygamefenster noch offen ist.

```python
def GenerationsEnde():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
```

Wenn die Generation abgelaufen ist, sammelt zuerst der [GarbageCollecter](https://docs.python.org/3/library/gc.html) die nicht mehr genutzten Objekte ein, sodass der Arbeitsspeicher entlastet wird und die gesamte Simulation somit flüssiger laufen kann.
Die Generationsanzahl wird um 1 erhöht und der Zeitwert (die Ticks) wieder auf 200 gesetzt.
Nun wird die leere Liste "Überlebende" initialisiert.

```python
if Generation[1] < 0:
  # Die nicht mehr genutzten Objekte werden durch den Garbage Collecter gelöscht, sodass die ganze Simulation flüssiger läuft.
  gc.collect()
  # Die Generationsanzahl wird um 1 erhöht
  Generation[0] += 1
  # Die ablaufenden Zeitwerte (Ticks) werden wieder auf 200 gesetzt
  Generation[1] = Generation[2]
  # Eine neue Liste mit den überlebenden Wesen, die es in die Safezone geschafft haben, wird initialisiert
  Überlebende = []
```

## Die Vererbung der Gene

Die Hauptfunktion dieser Simulation stellt die Vererbung der angepasstesten Gene, womit ein Wesen mit hoher Wahrscheinlichkeit die Safezone erreichen kann, dar.
Damit das Ganze ohne Probleme ablaufen kann, wird die leere Liste `Überlebende` erstellt.
Nun wird die Position jedes Wesens mit den Koordinaten der Safezone überprüft und wenn eine Übereinstimmung der x- und y-Koordinate besteht, wird ein neues Wesen erschaffen. Dieses Objekt (Wesen) wird mit der Genomgröße 0 erschaffen, da es keine zufälligen anfänglichen Gene erhalten soll.
Das Wesen, dessen Koordinaten mit denen der Safezone übereinstimmten, hat nun die Ehre, seine Gene an das neu erschaffene Wesen zu vererben. <br>
Dieses neue Wesen, welches nun die Gene vererbt bekommen hat, mit denen ein anderes Wesen in der vorigen Generation die Safezone erreicht hat, wird nun an die Liste der `Überlebenden` angehängt.
Die `WesenListe` (Liste aller Wesen einer Generation) wird geleert und die Anzahl der Überlebenden wird mit der Anzahl der Werte in der `Überlebenden` Liste in der Konsole ausgegeben.
Nun müssen für die neue Generation neue Wesen geschaffen und der WesenListe angehängt werden.
Die Gesamtanzahl (standardmäßig 200) der Wesen in der Simulation wird wieder einem temporären Wert zugewiesen und solange dieser größer 0 ist, wird aus der Liste der überlebenden Wesen ein zufälliges Wesen ausgewählt, das einem neu erschaffenen Wesen, seine Gene vererbt. Nach jeder Vererbung wird der temporäre Wert um 1 verringert. <br>
Jedes neue Wesen mit "guten Genen" wird an die WesenListe angehängt und ist in der nächsten Generation dabei.

```python
for i, creature in enumerate(WesenListe):
  for x, Safespot in enumerate(Safezone):
    # Bei jedem Wesen wird geprüft, ob die Koordinaten(Position) mit denen der Safezone übereinstimmen
    if creature.pos[0] == Safespot[0] and creature.pos[1] == Safespot[1]:
      # Wenn das Ganze zutrifft, wird ein neues Wesen erschaffen
      # Dieses Wesen wird ohne Gene erschaffen
      neuesWesen = Wesen(0)
      for j, genom in enumerate(creature.Gene):
        # Das überlebende Wesen vererbt seine Gene an das neuerschaffene Wesen
        neuesWesen.Gene.append(gene([genom.x_gen[0], genom.x_gen[1]], [genom.y_gen[0], genom.y_gen[1]], genom.z_gen))
      # Somit lässt sich eine Liste der Überlebenden mitsamt ihren Genen erstellen
      Überlebende.append(neuesWesen)
    # Die Liste der Wesen wird nach jeder Generation geleert
    WesenListe = []
    # Die Anzahl der Wesen in der Liste der Überlebenden wird ausgegeben
    print('Anzahl der Überlebenden:' + str(len(Überlebende)))
    Temp = GesamtAnzahl
    # Für jedes der Wesen (in unserem Beispiel 200)
    while Temp > 0:
      # Ein Wesen wird aus der Liste der Überlebenden ausgewählt
      AuserwähltesWesen = Überlebende[random.randrange(len(Überlebende))]
      neuesWesen = Wesen(0)
      for j, genom in enumerate(AuserwähltesWesen.Gene):
        # Und Erbinformationen (Bewegung, Farbe, etc.) werden an ein anderes Wesen weitergegeben
        # Starke/gute Gene, mit denen ein Wesen in der vorigen Generation die Safezone erreicht hat, werden weitergegeben
        neuesWesen.Gene.append(gene([genom.x_gen[0], genom.x_gen[1]], [genom.y_gen[0], genom.y_gen[1]], genom.z_gen))
        # Das neue Wesen wird zur Liste der Wesen hinzugefügt
      WesenListe.append(neuesWesen)
      # Das Ganze geht so lange, bis durch alle Wesen durch iteriert wurde
      Temp -= 1
```

# Die Main-Funktion und Initialisierung aller Variablen

Nun sind wir am Ende des Programmes angelangt. Alle Objekte, Funktionen und jedes klitzekleine Detail wurden erklärt und nun fragt man sich, was denn überhaupt noch fehlen kann, wo doch bereits knapp 400 Zeilen Quelltext überstanden sind. Um kurz auf die Frage zu antworten: Die Main-Funktion. <br>
Als Main wird in jeder Programmiersprache die Funktion bezeichnet, in der alle Funktionen, Klassen, Objekte und Sonstiges zusammengefügt und letztendlich ausgeführt werden. Das ist in unserem Projekt auch der Fall. In dieser Funktion werden auch die ganzen "verstellbaren" Variablen, welche als Parameter für die zahlreichen Funktionen dienen, initialisiert. Man kann beispielsweise die Länge einer Generation verändern, die Größe des Fensters oder der Safezone, die Gesamtanzahl der Wesen oder die Genomgröße. Diese Änderungen haben eine globale Wirkung.
Normalerweise bleiben Variablen bzw. die Werte, die Variablen in einer Funktion zugewiesen werden, lokal in dieser Funktion. 
Das Schlüsselwort `global` legt jedoch fest, dass die Änderungen, die man an den, mit diesem Schlüsselwort bezeichneten Variablen vornimmt, im gesamten Programm wirksam sind.
Alle wichtigen zu initialisierenden Variablen, die wir in unserem Programm an verschiedensten Stellen benötigen, sind als `global` in der Main-Funktion deklariert.
```python
global WesenListe, Generation, Größe, GenomGröße, PositionsListe, Safezone, Überlebende, GesamtAnzahl
```
Als erste Funktion wird `pygame.init()` ausgeführt, um alle Module Pygames zu initialisieren und den Prozess zu starten.
Daraufhin werden alle Variablen initialisiert.
Die besondere Festlegung der Safezone wird in der [Initialisierung der Safezone](#die-initialisierung-der-safezone) genauestens erklärt.
Danach folgt auch schon die Generierung der Wesen durch die Funktion `generieren()`.
Das Pygamefenster, welches als Parameter für die [*renderFenster-Funktion*](#das-rendering) dient, wird nun auch festgelegt.
Dazu auch noch der Fenstertitel: **"Survival of the fittest - Wer ist am besten angepasst?"** und schon kommt die eigentliche Ausführung des ganzen Programms.
Eigentlich kann das Programm, wenn es nicht vorher abgebrochen wird, auf immer und ewig weiterlaufen, da es sich in einem endlosen while-True-Loop befindet.
Zuerst gibt es eine Pause von 5ms und daraufhin wird das Fenster gerendert, die Simulation beendet und daraufhin wieder gestartet.
Dieser Ablauf wiederholt sich dauerhaft.
Nun bleibt nur noch eine Frage offen:<br>
_Wofür stehen denn diese letzten beiden Zeilen?_
```python
if __name__ == "__main__":
  main()
``` 
In Python beschreibt diese Bedingung, dass die `Main-Funktion`, die in der Bedingung steht, nur ausgeführt werden soll, wenn die Datei als Skript ausgeführt wird.
Es gebe auch die Möglichkeit, die Datei als Modul in eine andere Datei zu importieren. Dann würde das, was in der Bedingung steht, nicht ausgeführt werden, da die Datei nicht als `Hauptdatei`, sondern als `Modul` ausgeführt wird.
Eigentlich wäre dieser Zusatz nicht nötig, da dieses Projekt nur auf einer Datei beruht, jedoch ist es eine gute Angewohnheit, Hauptdateien` (Main-Dateien) mit dieser Bedingung am Ende zu versehen, da sich das Ganze positiv auf zukünftige Projekte, wo vielleicht mit selbstgeschriebenen Modulen gearbeitet wird, auswirkt.
```python
def main():
    # Deklarierung der Variablen als Global, sodass jedes Objekt und jede Funktion darauf zugreifen kann
    global WesenListe, Generation, Größe, GenomGröße, PositionsListe, Safezone, Überlebende, GesamtAnzahl
    # Initialisierung Pygames
    pygame.init()
    # In dieser Liste werden alle Wesen gespeichert
    WesenListe = []
    # Von jedem Wesen werden 8 Positionen gespeichert, sodass die Bewegung nachverfolgbar ist (s. Schweif im GitHub Repository)
    PositionsListe = [[], [], [], [], [], [], [], []]
    # Alle überlebenden Wesen werden in dieser Liste gespeichert
    Überlebende = []
    # [Aktuelle Generation, Ablaufende Ticks, Standard-Zeitwert für die ablaufenden Ticks]
    # Eine Generation dauert 200 Ticks, es sei denn, die Wesen bewegen sich vorher nicht mehr.
    # Danach werden die ablaufenden Ticks (Generation[1]) wieder auf 200 gesetzt und das Ganze beginnt von Neuem
    Generation = [1, 200, 200]
    # Größe des Simulationsbereiches
    Größe = [100, 100]
    # Anzahl der Wesen
    GesamtAnzahl = 200
    # Beinhaltet alle Pixel, die die Safezone markieren
    Safezone = []
    SafezoneX = Größe[0] - 1
    while SafezoneX >= 0:
        SafezoneY = Größe[1] - 1
        while SafezoneY >= 0:
            # Über die Intervalle für X und Y lässt sich die Safezone bestimmen
            # Es wird von 100 bis 0 iteriert und, wenn sich SafezoneX/SafezoneY im Safezone-Bereich befinden, werden diese der Safezone Liste angehängt
            if SafezoneX >= 0 and SafezoneX <= 30 and SafezoneY >= 0 and SafezoneY <= 30:
                # Die Safezone Pixel werden festgehalten
                Safezone.append([SafezoneX, SafezoneY])
            SafezoneY -= 1
        SafezoneX -= 1
        # print(SafezoneX)
        # print(SafezoneY)
    # Die Größe (Komplexität in der Berechnung) des Erbguts wird festgelegt. Je größer, desto komplizierter der Organismus (Beispiel: Bakterium = 1
    #                                                                                                                                 Mensch = 1000)
    GenomGröße = 10

    # Mit den initialisierten (Variablen)Parametern werden die Wesen generiert
    generieren()

    # Die Fenstergröße wird festgelegt (Der Faktor 8 und der Summand 59 fungiert wieder als Anpassung an die Größe des Pygame Fensters)
    Fenster = pygame.display.set_mode((Größe[0] * 8 + 59, Größe[1] * 8 + 59))

    # Fenstertitel: 'Survival of the fittest - Wer ist am besten angepasst ?' wird festgelegt
    pygame.display.set_caption('Survival of the fittest - Wer ist am besten angepasst ?')

    # Während das Programm läuft, gibt es nach jeder Generation eine 5ms Pause.
    # Daraufhin wird das Fenster gerendert, überprüft, ob die Simulation überhaupt noch läuft und dann die simulationStart-Funktion aufgerufen
    while True:
        pygame.time.delay(5)
        renderFenster(Fenster)
        GenerationsEnde()
        simulationStart()
    pass


if __name__ == "__main__":
    main()
```

# Quellenverzeichnis

### Inspiration

- [Conway's Spiel des Lebens](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens "Conway's Spiel des Lebens")

### Biologische Quellen

- [Genomgröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe)
- [Genom](https://de.wikipedia.org/wiki/Genom)

### Quellen 
- [Carbon für die schöne Darstellung des Quelltextes in der Dokumentation](https://www.carbon.now.sh)
- [Pygame Dokumentation](https://www.pygame.org/docs/)
- [Canva für die Erstellung von Grafiken](https://www.canva.com/)
### 

# Eigenständigkeitserklärung

Hiermit erklären wir, dass das Projekt selbstständig bearbeitet wurde und keine anderen als die angegebenen Quellen benutzt wurden. <br>
Ahrensburg, den 02. Dezember 2022 <br>
Laurenz Brause und Daniel Pauli

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />Dieses Werk ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Namensnennung - Nicht kommerziell - Keine Bearbeitungen 4.0 International Lizenz</a>
