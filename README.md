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

## Das Wesen

In unserer Simulation gibt es eine einstellbare Anzahl an Wesen. 
Jedes Wesen ist als Objekt definiert und besitzt einen Parameter Genomgröße.
Die [GenomGröße](https://de.wikipedia.org/wiki/Genomgr%C3%B6%C3%9Fe) beschreibt die Menge der Genome.
Ein [Genom](https://de.wikipedia.org/wiki/Genom) beinhaltet die Gesamtheit der vererbbaren Informationen einer Zelle.
Ein "Datensatz" Ergbut, der in einem Genom gespeichert wird, besteht aus drei verschiedenen [Genen](#die-gene).
Einem X-Gen, welches in zwei Werte aufgeteilt ist und einen zufälligen Wert zwischen 0 und 1 beinhaltet.
Einem Y-Gen, welches auch in zwei Werte aufgeteilt ist und einen zufälligen Wert zwischen 0 und 7 hat.
Und einem Z-Gen, welches lediglich einen Wert hat und dieser zufällig zwischen 0 und 8 ausgewählt.

...Grafik von Canva über Genom...

# Die Gene

Das Objekt "gene" beschreibt eine Liste bestehend aus drei verschiedenen Gentypen, die auch als Parameter übergeben werden.
Das X-Gen, Y-Gen und Z-Gen. Wie diese Gene initiiert werden (also, wie sie beispielsweise in zwei Werte geteilt werden oder welche Werte ihnen gegeben werden) ist
bis dato nicht festgelegt. 

![carbon (5)](https://user-images.githubusercontent.com/65679099/200275275-d3680b1c-8089-41f4-97be-e89226b3c53b.png)
