from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import json

app = Flask("tipps_chur")


@app.route('/', methods=["get", "post"])
def tipps_chur():
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.

    #neue Idee annehmen und dann in Datenbank abspeichern
    if request.method == "POST":
        name = request.form['name']
        gruppengroesse = request.form['Gruppengroesse']
        budget = request.form['Budget']
        saison = request.form['Saison']
        ort = request.form['Ort']
        bewegungsdrang = request.form['Bewegungsdrang']

        def abspeichern(name, gruppengroesse, budget, saison, ort, bewegungsdrang):
            datei_name = "datenbank_ideen.json"
            zeitpunkt = datetime.now()
            abspeichern(datei_name, name, gruppengroesse, budget, saison, ort, bewegungsdrang)
            return name, gruppengroesse, budget, saison, ort, bewegungsdrang

        abspeichern(name, gruppengroesse, budget, saison, ort, bewegungsdrang)

    return render_template("index.html", seitentitel="neue_idee")


if __name__ == "__main__":
    app.run(debug=True, port=5001)

