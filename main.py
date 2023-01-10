from flask import Flask
from flask import render_template, url_for
from flask import request
from datetime import datetime
import plotly.express as px
from plotly.offline import plot
import plotly
import json

app = Flask("tipps_chur")

@app.route('/', methods=["GET", "POST"])
def tipps_chur():
    if request.method == "POST":
        gruppengroesse_vorschlag = request.form['Gruppengroesse']
        budget_vorschlag = request.form['Budget']
        saison_vorschlag = request.form['Saison']
        ort_vorschlag = request.form['Ort']
        bewegungsdrang_vorschlag = request.form['Bewegungsdrang']
        with open("datenbank_ideen.json") as datei:
            ideen = json.load(datei)

        vorschlaege = []
        for idee_name, idee_daten in ideen.items():
            print(gruppengroesse_vorschlag, idee_daten["gruppengroesse"], gruppengroesse_vorschlag == idee_daten["gruppengroesse"])
            if gruppengroesse_vorschlag == idee_daten["gruppengroesse"]:
                if budget_vorschlag == idee_daten["budget"]:
                    if saison_vorschlag == idee_daten["saison"]:
                        if ort_vorschlag == idee_daten["ort"]:
                            if bewegungsdrang_vorschlag == idee_daten["bewegungsdrang"]:
                                vorschlaege.append(idee_daten)
        #Vorschläge werden zurückgegeben und Vorschläge html wird angezeigt
        return render_template("vorschlaege.html", vorschlaege=vorschlaege)

    return render_template("index.html", seitentitel="neue_idee")

#Code für Index Seite fertig


@app.route("/vorschlaege", methods=["GET", "POST"])
def vorschlaege():
    if request.method == "POST":
        ##hier Vorschlag in DIC abspeichern, wenn Wert vorhanden ist, dann Anzahl +1, wenn Wert nicht vorhanden ist, dann = neuer Eintrag
        gemachter_vorschlag = request.form.getlist('name')
        activity_getan = {'name': gemachter_vorschlag}
        activity_getan_speichern(activity_getan)

    return "Vorschlag wurde abgespeichert"
def activity_getan_speichern(activity_getan):
    datei_name = "datenbank_vorschlaege.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, activity_getan)
    return zeitpunkt, activity_getan

#ab hier Code für Seite neue Idee
@app.route('/neue_idee', methods=["GET", "POST"])
def neue_idee():
    # neue Idee annehmen und dann in Datenbank abspeichern
    if request.method == "POST":
        name = request.form.get('name')
        gruppengroesse = request.form['Gruppengroesse']
        budget = request.form['Budget']
        saison = request.form['Saison']
        ort = request.form['Ort']
        bewegungsdrang = request.form['Bewegungsdrang']

        activity = {'name': name, 'gruppengroesse': gruppengroesse, 'budget': budget, 'saison': saison, 'ort': ort, 'bewegungsdrang': bewegungsdrang}

        aktivitaet_speichern(activity)

    return render_template("neue_idee.html")

def speichern(datei, key, value):
    try:
        with open(datei, "r") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)
    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def aktivitaet_speichern(activity):
    datei_name = "datenbank_ideen.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, activity)
    return zeitpunkt, activity
#Code Seite neue Aktivität erfassen fertig

#ab hier Code für Seite Auswertung
@app.route('/auswertung', methods=["GET", "POST"])

def auswertung():
    div = viz()
    return render_template("auswertung.html", viz_div=div)
def viz():
    #hier Datenbank öffnen und umwandeln, damit ich diese in Balkendiagramm aufzeichnen kann
    auswertung_gespeichert = aktivitaeten_gespeichert_oeffnen()
    counts = {}
    for _, eintrag in auswertung_gespeichert.items():
        items = eintrag.get('name')
        for item in items:
           if item in counts:
               counts[item]+=1
           else:
               counts[item]=1

    # Grafik wird mit Variabel x als x-Wert und y als y-Wert erstellt.
    # counts = {'Wandern Calanda': 2, 'Wandern xyz': 10}

    fig = px.bar(x=list(counts.keys()), y=list(counts.values()))
    # Mit plotly.io.to_html wird die Grafik als div angezeigt.
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)

    # Analyse.html wird gerendert, div wird mitgegeben.
    return render_template('auswertung.html', viz_div=div)

def aktivitaeten_gespeichert_oeffnen():
    try:
        with open('datenbank_vorschlaege.json', 'r', encoding='utf-8') as datenbank_vorschlaege:
            # Inhalt der Datenbank wird als Dictonary vorschlaege_gespeichert gespeichert.
            vorschlaege_gespeichert = json.load(datenbank_vorschlaege)
    except:
        vorschlaege_gespeichert = {}

    return vorschlaege_gespeichert
#Code Seite Auswertungfertig

if __name__ == "__main__":
    app.run(debug=True, port=8000)