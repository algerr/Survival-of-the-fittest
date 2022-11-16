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
Ein "Datensatz" Ergbut, der in einem Genom gespeichert wird, besteht aus drei verschiedenen [Genen](#die-gene).
Einem X-Gen, welches in zwei Werte aufgeteilt ist und einen zufälligen Wert zwischen 0 und 1 beinhaltet.
Einem Y-Gen, welches auch in zwei Werte aufgeteilt ist und einen zufälligen Wert zwischen 0 und 7 hat.
Und einem Z-Gen, welches lediglich einen Wert hat und dieser zufällig zwischen 0 und 8 ausgewählt.

![Screenshot_20221107_111302](https://user-images.githubusercontent.com/111282979/202248021-fbc11b40-15dc-49b3-b351-b211b11420cd.png)

# Die Gene

Das Objekt "gene" beschreibt eine Liste bestehend aus drei verschiedenen Gentypen, die auch als Parameter übergeben werden.
Das X-Gen, Y-Gen und Z-Gen. Wie diese Gene initiiert werden (also, wie sie beispielsweise in zwei Werte geteilt werden oder welche Werte ihnen gegeben werden) ist
bis dato nicht festgelegt.

# Die Mutation

Jedes Wesen, welches in der Simulation während einer Generation vorhanden ist, besteht aus einer einstellbaren Genomenanzahl. Dabei hat jedes einzelne Genom zu Beginn der Runde einen zufälligen Mutationswert, welcher im Intervall [0;15] liegt. Abhängig von dem Mutationswert, bestimmt die Zahl, welches Gen genau mutiert. Wenn der Mutationswert "0" beträgt , mutiert das x0-Gen, bei einem Mutationswert von "1" hingegen das x1-Gen.enn der Wert im Intervall von [2;4] liegt, dann mutiert das y0-Gen und wenn die Zahl Im Intervall von [5;7] liegt das y1-gen. Wennn der Wertsogar im Intervall [8;15] liegen sollte , mutiert das z-Gen. Insgesammt ergibt sich auch dadurch, dass insgesammt betrachtet, Wahrscheinlichkeit, dass es zur Mutation kommt propotional zur Genomanzahl ist. Wenn man allerdings jedes Genom einzeln betrachtet, besteht hier die Wahrscheinlichkeit, dass ein Genom mutiert 1/50 also 2%. Eine Mutation kann sich zwar einserseits positiv auf das Überleben des Wesens auswirken, weil es die Bewegungsart zufällig verändert. Gleichzeitig kann eine Mutation aber auch negative Folgen mit sich bringen, weil alles auf dem Zufall beruht.


![carbon (5)](https://user-images.githubusercontent.com/65679099/200275275-d3680b1c-8089-41f4-97be-e89226b3c53b.png)

# Die zufällige Bewegung der Wesen

Die Bewegung jedes Wesens steht in Abhängigkeit zu dessen Genen.
Je nachdem, welches X-, Y-, und Z-Gen vorhanden ist und auf welcher Höhe und Breite sich das Wesen befindet, bewegt sich das Wesen schneller oder langsamer nach oben, unten, links oder rechts.

## Der Simulationsbeginn

Sobald die Simulation startet, wird zuerst abgefragt, ob die Generation noch läuft.
Daraufhin wird bei jedem Tick der Generation (von 200 bis 1) durch die Liste der Wesen iteriert und für jedes Wesen ein "stabiler Wert" definiert.
Dazu wird auch eine Variable mit dem Namen "Veränderung" definiert, die die aktuelle Position, den Zeitwert, 
Dieser "stabile Wert" wird im Folgenden dazu genutzt, die "Veränderung" zu speichern.

