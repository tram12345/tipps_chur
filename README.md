## 1 Problembeschreibung/Motivation
In der Webapplikation stehen verschiedene Kriterien zur Auswahl. Insgesamt sind es 6 Kriterien, die man auswählen kann. 
Aufgrund dieser Auswahl werden einem Tipps für Aktivitäten rund um und in Chur vorgeschlagen. 
Die Kriterien, welche man auswählen kann, sind: 
- Gruppengrösse
- Budget
- Saison
- Ort
- Bewegungsdrang
Anschliessend werden einem die passenden Vorschläge angezeigt.

Bei den vorgeschlagenen Aktivitäten kann dann die Aktivität, welche man unternehmen möchte, auswählen 
und diese wird dann abgespeichert. 

Falls keine passende Aktivität gefunden wurde, kann eine neue Aktivität hinterlegt werden. 

Ebenfalls werden alle bisher getätigten Aktivitäten mit einem Balkendiagramm dargestellt, welche Aktivität, wie viel mal getätigt wurde. 


## 2 Betrieb
Als erstes muss mithilfe der Ausführung des Codes (main Python Datei) Flask und Plotly importiert werden. 
Ansonsten muss bei der Ausführung des Codes auf nichts besonderes geachtet werden. 

## 3 Benutzung
Das Projekt wird genutzt indem man die einzelnen Kriterien auswählt und ein Vorschlag dann generiert wird.
Diese Vorschläge werden dann, wenn sie ausgewählt werden, abgepseichert und ausgewertet.
Findet man keine passende Vorschläge hat man die Möglichkeit eine neue Aktivität hinzufügen. 
Es besteht die Option ein Vorschlag zu generieren, eine neue Aktivität zu erfassen und eine Auswertung der bereits getätigten Aktivitäten anzuschauen.


## 4 Architektur

<img src="C:\Users\tamar\OneDrive - Jansen AG\FHGR-DESKTOP-KU2T1ET\3. Semester\RPOG2\tipps_chur\images\ablaufdiagramm.drawio.png"/>

## 5 Ungelöste/unbearbeitete Probleme
Es wurde nicht gelöst, dass die Aktivitäten mit Kommentar und Bewertung in einem Dictionary abgespeichert werden. 
Man könnte sicher das Design noch verschöndern und eventuell die Akvitiäten um weitere Kriterien ergänzen. 