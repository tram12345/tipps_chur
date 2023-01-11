## 1 Problembeschreibung/Motivation
In der Webapplikation stehen verschiedene Kriterien zur Auswahl. 
Insgesamt sind es fünf Kriterien, die man auswählen kann. 
Aufgrund der getätigten Auswahl werden einem Tipps für Aktivitäten rund um und in Chur vorgeschlagen. 
Die Kriterien, welche man auswählen kann, sind: 
- Gruppengrösse
- Budget
- Saison
- Ort
- Bewegungsdrang
Anschliessend werden einem die passenden Vorschläge generiert und angezeigt.

Bei den vorgeschlagenen Aktivitäten kann dann die Aktivität, welche man unternehmen möchte, ausgewählt werden und diese wird dann abgespeichert. 

Falls keine passende Aktivität gefunden wurde, kann eine neue Aktivität hinterlegt werden. 

Ebenfalls werden alle bisher getätigten Aktivitäten mit einem Balkendiagramm dargestellt, welche Aktivität, wie viel mal getätigt wurde. 


## 2 Betrieb
Als erstes muss mithilfe der Ausführung des Codes (main Python Datei) Flask und Plotly importiert werden. 
Ansonsten muss bei der Ausführung des Codes auf nichts besonderes geachtet werden. 

## 3 Benutzung
Das Projekt wird genutzt, indem man die einzelnen Kriterien auswählt und ein Vorschlag generiert wird.
Diese Vorschläge werden dann, wenn sie ausgewählt wurden, abgepseichert und ausgewertet.
Findet man keine passende Vorschläge hat man die Möglichkeit eine neue Aktivität hinzuzufügen. 
Es besteht die Option, ein Vorschlag zu generieren, eine neue Aktivität zu erfassen und eine Auswertung der bereits getätigten Aktivitäten anzuschauen.


## 4 Architektur
![Ablaufdiagramm](../master/images/ablaufdiagramm.png)

## 5 Ungelöste/unbearbeitete Probleme
Es wurde nicht gelöst, dass die Aktivitäten mit Kommentar und Bewertung in einem Dictionary abgespeichert werden. 
In einem weiteren Schritt könnte man das Design verschönern und die User Experience erhöhen. 