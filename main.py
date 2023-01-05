from flask import Flask
from flask import render_template, url_for
from flask import request
from datetime import datetime
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

    # Rendern des index.html Templates, für das Anzeigen der index.html Page.
    return render_template("index.html", seitentitel="neue_idee")


@app.route('/neue_idee', methods=["GET", "POST"])
def neue_idee():
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.
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
        with open(datei) as open_file:
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



@app.route('/auswertung', methods=["GET", "POST"])
def auswertung():
    return render_template("auswertung.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)