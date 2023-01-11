from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import plotly.express as px
import plotly
import json

app = Flask("tipps_chur")

#ab hier Code für Seite "Ideenvorschläge generieren"
@app.route('/', methods=["GET", "POST"])
def tipps_chur():
    #Code nimmt hier die Einträge der Eingabefelder entgegen und diese werden in Variablen umgewandelt
    if request.method == "POST":
        gruppengroesse_vorschlag = request.form['Gruppengroesse']
        budget_vorschlag = request.form['Budget']
        saison_vorschlag = request.form['Saison']
        ort_vorschlag = request.form['Ort']
        bewegungsdrang_vorschlag = request.form['Bewegungsdrang']
        #Datenbank wird geöffnet und Inhalt wird in ideen abgespeichert
        with open("datenbank_ideen.json") as datei:
            ideen = json.load(datei)

        #hier wird überprüft, welche Aktivitäten zur Idee passen, aber zuerst wird eine leere Liste Vorschläge erstellt
        vorschlaege = []
        for idee_name, idee_daten in ideen.items():
             if gruppengroesse_vorschlag == idee_daten["gruppengroesse"]:
                if budget_vorschlag == idee_daten["budget"]:
                    if saison_vorschlag == idee_daten["saison"]:
                        if ort_vorschlag == idee_daten["ort"]:
                            if bewegungsdrang_vorschlag == idee_daten["bewegungsdrang"]:
                                #nach der Überprüfung werden die übereinstimmenden Felder in die  Liste Vorschläge hinzugefügt
                                vorschlaege.append(idee_daten)
        #vorschlaege wird zurückgegeben und Vorschläge html wird angezeigt
        return render_template("vorschlaege.html", vorschlaege=vorschlaege)

    #index_html wird zurückgegeben
    return render_template("index.html", seitentitel="neue_idee")
#Code für Seite "Ideenvorschläge generieren" fertig


#ab hier Code für Seite "Vorschläge"
@app.route("/vorschlaege", methods=["GET", "POST"])
def vorschlaege():
    if request.method == "POST":
        #angeklickter Vorschlag wird zurückgegeben und wird mithilfe der Funktion abgespeichert
        gemachter_vorschlag = request.form.getlist('name')
        activity_getan = {'name': gemachter_vorschlag}
        activity_getan_speichern(activity_getan)
    #abgespeichert_vorschlag HTML wird angezeigt
    return render_template("abgespeichert_vorschlag.html")

#Funktion um den angeklickten Vorschlag in der Datenbank abzuspeichern
def activity_getan_speichern(activity_getan):
    datei_name = "datenbank_vorschlaege.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, activity_getan)
    return zeitpunkt, activity_getan

#ab hier Code für Seite "neue Idee erfassen"
@app.route('/neue_idee', methods=["GET", "POST"])
def neue_idee():
    # hier wird eine neue Idee angenommen und dann in der Datenbank abgespeichert
    if request.method == "POST":
        #Felder werden von dem Formular geholt
        name = request.form.get('name')
        gruppengroesse = request.form.get('Gruppengroesse')
        budget = request.form.get('Budget')
        saison = request.form.get('Saison')
        ort = request.form.get('Ort')
        bewegungsdrang = request.form.get('Bewegungsdrang')
        #Felder werden in ein Dictionary umgewandelt
        activity = {'name': name, 'gruppengroesse': gruppengroesse, 'budget': budget, 'saison': saison, 'ort': ort, 'bewegungsdrang': bewegungsdrang}
        #Funktion aktivitaet_speichern wird ausgeführt
        aktivitaet_speichern(activity)
    #neue Idee HTML wird zurückgegeben
    return render_template("neue_idee.html")

#Funktion um die eingegebene neue Idee abzuspeichern
def aktivitaet_speichern(activity):
    datei_name = "datenbank_ideen.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, activity)
    return zeitpunkt, activity
#Code Seite "neue Idee erfassen" fertig

#ab hier Code für Seite "Auswertung"
@app.route('/auswertung', methods=["GET", "POST"])
def auswertung():
    # hier wird die Funktion um die Datenbank zu öffnen, ausgeführt und die Daten werden umgewandelt, damit diese in einem Balkendiagramm aufgezeichnet werden
    auswertung_gespeichert = aktivitaeten_gespeichert_oeffnen()
    # leeres Dictionary wird erstellt
    counts = {}
    # for-loop für alle values
    for _, eintrag in auswertung_gespeichert.items():
        #name der Aktivität wird genommen und in Variable items umgewandelt
        items = eintrag.get('name')
        #for loop für alle items wird ausgeführt
        for item in items:
            #wenn item schon in counts ist, dann wird die Anzahl des items um eins erhöht
            if item in counts:
                counts[item] += 1
            #wenn es das item noch nicht gibt, dann wird das item hinzugefügt und die Anzahl ist eins
            else:
                counts[item] = 1

    #counts Liste sieht so aus und diese werden dann in Balkendiagramm angezeigt
    #counts = {'Wandern Calanda': 2, 'Wandern xyz': 10}
    fig = px.bar(x=list(counts.keys()), y=list(counts.values()))
    #mit plotly.io.to_html wird die Grafik als div angezeigt.
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)

    #auswertung HTML wird angezeigt und div wird mitgegeben.
    return render_template('auswertung.html', viz_div=div)


#hier wird die Datei mit den gespeicherten Aktivitäten geöffnet
def aktivitaeten_gespeichert_oeffnen():
    try:
        with open('datenbank_vorschlaege.json', 'r', encoding='utf-8') as datenbank_vorschlaege:
            #Inhalt der Datenbank wird als Dictionary datenbank_vorschlaege gespeichert.
            vorschlaege_gespeichert = json.load(datenbank_vorschlaege)
    except:
        #wenn kein Eintrag, wird es als leeres Dictionary gespeichert
        vorschlaege_gespeichert = {}

    return vorschlaege_gespeichert
#Code Seite Auswertung fertig


#allgemeine speichern Funktion, um die Einträge in den Datenbanken abzuspeichern
def speichern(datei, key, value):
    try:
    #Datei wird probiert zum Öffnen wenn nicht klapp dann wird ein leerer Datei Inhalt reingeschrieben
        with open(datei, "r") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    #print(datei_inhalt)
    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

if __name__ == "__main__":
    app.run(debug=True, port=8000)