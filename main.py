from flask import Flask
from flask import render_template, url_for
from flask import request
from datetime import datetime
import json

app = Flask("tipps_chur")


@app.route('/', methods=["get", "post"])
def tipps_chur():
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

        #hier noch alle Felder hinzufügen!!!!!
        activity = {'name': name, 'budget': budget}

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


def aktivitaet_speichern(aktivitaet):
    datei_name = "datenbank_ideen.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet

if __name__ == "__main__":
    app.run(debug=True, port=8000)

