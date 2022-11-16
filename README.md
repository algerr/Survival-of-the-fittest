![🟥Survival_of_the_fittest🟩](https://user-images.githubusercontent.com/65679099/199816912-d8de71a4-db2a-4827-b88d-c63ec379cfdb.png)

![image](https://user-images.githubusercontent.com/65679099/199478187-8c3a0b3c-76b7-4fb8-9c23-724da39c42ee.png)

## Der Hintergrund

Wie durch die Chronologie der Blogeinträge bereits erkennbar wurde, war dieses Projekt nicht das erste, an welchem wir gearbeitet haben. Leider scheiterte die Umsetzung als Mobilapp durch die Kosten von 100€ für einen Apple-Developer Account. Nachdem wir zu dieser Erkenntnis gelangen, suchten wir nach einem neuen Projekt.
Einflussreich waren dabei der Biologieunterricht des vergangenen Jahres sowie [Conway's Spiel des Lebens](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens "Conway's Spiel des Lebens").

## Das Grundprinzip

Das Programm stellt eine Evolution dar. Wesen mit unterschiedlichen Genen geben ihr Bestes, um die grünmarkierte Safezone zu erreichen. Wer am Ende der Generation die Zone erreicht hat, gibt seine Gene an die nächste Generation weiter.
Zu Beginn erhalten alle Wesen ein zufälliges Erbgut.
Dieses besteht aus X-Genen, Y-Genen und Z-Genen.
Wie in der menschlichen DNA gibt sind die Gene zweigeteilt. X[1] und X [2] sowie Y[1] und Y[2] nur Z hat lediglich einen Wert. 
Davon abhängig sind die Bewegung jedes einzelnen Wesens und seine Farbe.
Nun gilt: Wessen Gene es in die Safezone schaffen, werden weitergegeben.
Somit werden zunehmend Wesen mit ähnlichen Genen übrig bleiben, die fast alle die Safezone erreichen.

## Die Initialisierung des Pygame-Fensters

Die Simulation lässt sich natürlich komplett über Mathematik und Daten veranschaulichen. Da diese Simulation jedoch davon lebt, in Echtzeit mitverfolgt zu werden.

## Das Wesen

In unserer Simulation gibt es eine einstellbare Anzahl an Wesen. 
Jedes Wesen ist als Objekt definiert und besitzt einen Parameter Genomgröße.
Die [GenomGröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe) beschreibt die Menge der Genome.
Ein [Genom](https://de.wikipedia.org/wiki/Genom) beinhaltet die Gesamtheit der vererbbaren Informationen einer Zelle.
Ein "Datensatz" Ergbut, der in einem Genom gespeichert wird, besteht aus drei verschiedenen [Genen](#das-genom).
Einem X-Gen, welches in zwei Werte aufgeteilt ist und einen zufälligen Wert zwischen 0 und 1 beinhaltet.
Einem Y-Gen, welches auch in zwei Werte aufgeteilt ist und einen zufälligen Wert zwischen 0 und 7 hat.
Und einem Z-Gen, welches lediglich einen Wert hat und dieser zufällig zwischen 0 und 8 ausgewählt.

# Das Genom

Das Objekt "Genom" beinhaltet drei verschiedenen Gentypen, die auch als Parameter übergeben werden.
Das X-Gen, Y-Gen und Z-Gen. Wie diese Gene initiiert werden (also, wie sie beispielsweise in zwei Werte geteilt werden oder welche Werte ihnen gegeben werden) ist
bis dato nicht festgelegt.

![Screenshot_20221107_111302](https://user-images.githubusercontent.com/111282979/202248021-fbc11b40-15dc-49b3-b351-b211b11420cd.png)

# Die Mutation

Jedes Wesen besitzt eine einstellbare [GenomGröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe). 
Damit die ganze Genetik noch realistischer ist, können die Gene jedes Genoms nun mit einer Wahrscheinlichkeit von 2% mutieren. Dabei hat jedes einzelne Genom zu Beginn der Runde einen zufälligen Mutationswert, welcher im Intervall [0;15] liegt. Abhängig von dem Mutationswert, bestimmt die Zahl, welches Gen genau mutiert. Wenn der Mutationswert "0" beträgt , mutiert das x0-Gen, bei einem Mutationswert von "1" hingegen das x1-Gen.Wenn der Wert im Intervall [2;4] liegt, dann mutiert das y0-Gen und wenn die Zahl Im Intervall [5;7] liegt das y1-gen. Wennn der Wert sogar im Intervall [8;15] liegen sollte , mutiert das z-Gen. Insgesammt lässt sich abschließend betrachten, dass die Anzahl der Gesammtmutationen propotional zur Genomanzahl ist. Wenn man allerdings jedes Genom einzeln betrachtet, ist hier die Wahrscheinlichkeit konstant, dass ein Genom zu 1/50 also 2% mutiert. Eine Mutation kann sich zwar einserseits positiv auf das Überleben des Wesens auswirken, weil es die Bewegungsart zufällig verändert. Gleichzeitig kann eine Mutation aber auch negative Folgen mit sich bringen, weil alles auf dem Zufall beruht.


![carbon (3)](https://user-images.githubusercontent.com/111282979/202264782-4efa0eb5-03d5-4eee-bb0a-ca62f8339708.png)



# Die zufällige Bewegung der Wesen

Die Bewegung jedes Wesens steht in Abhängigkeit zu dessen Genen.
Je nachdem, welches X-, Y-, und Z-Gen vorhanden ist und auf welcher Höhe und Breite sich das Wesen befindet, bewegt sich das Wesen schneller oder langsamer nach oben, unten, links oder rechts.

## Der Simulationsbeginn

Sobald die Simulation startet, wird zuerst abgefragt, ob die Generation noch läuft.
Daraufhin wird bei jedem Tick der Generation (von 200 bis 1) durch die Liste der Wesen iteriert und für jedes Wesen ein "stabiler Wert" definiert.
Dazu wird auch eine Variable mit dem Namen "Veränderung" definiert, die die aktuelle Position, den Zeitwert, 
Dieser "stabile Wert" wird im Folgenden dazu genutzt, die "Veränderung" zu speichern.

### Überprüfung der Validität

Da die Simulation, um schöne Ergebnisse mit dennoch komplexen Genen zu erhalten, viele Generationen durchlaufen muss, wäre es ziemlich schade, wenn auf einmal, ein Fehler, bezüglich der Koordinaten eines Wesens, auftreten würde.
Dafür haben wir eine Funktion "überprüfeValidität" mit den Parametern "(x, y)" definiert, die überprüft, dass die Koordinaten jedes Wesens im Simulationsfenster liegen.
Dazu ist es aber auch ungünstig, wenn sich mehrere Wesen auf dem gleichen Feld befinden können, da somit der Konkurrenzkampf darunter leidet.
Infolgedessen, wird noch überprüft, ob die x- und y-Position jedes Wesen mit den übergebenen Werten übereinstimmt.
Sollte das der Fall sein, wird ein False-Statement zurückgegeben, sodass die eingegebenen Werte keine validen Positionen sein können.
Wenn keine Äquivalenz zu den Positionen eines anderen Wesens vorliegt, wird ein True-Statement zurückgegeben und die eingegebenen Werte sind valide Positionen.

![überprüfeValiditätCarbon](https://user-images.githubusercontent.com/65679099/202256158-ccb9bd2e-1091-47c0-8350-b7cf945b668c.png)


## Safezone

Die Safezone ist die grün gekennzeichnete Fläche, welche auch das "Zielfeld" markiert, in welchem sich die Wesen bis zum Ende einer Generation befinden sollten, damit sie ihre Gene weitergeben. Die Wesen wissen nicht, wo sich die Safezone genau befindet und sind deshalb auf ihre Bewegungsart angewiesen bzw. müssen hoffen, dass sie durch ihre Bewegungsart die Zone bis zum Ende einer Generation erreichen. Die Wesen, welche es rechzeitig schaffen die Safezone zu erreichen, geben ihre Gene und somit auch ihre Bewegungsart weiter, damit in der nächsten Generation die neu entstandenen Wesen, welche jetzt hauptsächlich die Bewegungsart ihrer Vorfahren übernommen haben, ebenfalls die Safezone erreichen. Dieser Vorgang wiederholt sich immer wieder, wobei gehofft wird, dass irgendwann alle Individuen die Safezone erreichen.
Das ist jedoch unmöglich, da Mutationen immer auftreten können oder manche sich direkt zu Beginn in der Safezone befinden und sich überhaupt nicht bewegen, sodass ihr Überleben durch das Feld, in dem sie erscheinen, abhängt. Die Safezone verändert sich von Generation zu Generation nicht, weil die Weitergabe der erfolgreichen Bewegungsart, keinen Sinn ergibt, wenn sich die Safezone mit jedem Mal ändert. Dann würden sich die Wesen beispielsweise in die komplett falsche Richtung bewegen.
