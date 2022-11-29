from flask import Flask
from flask import render_template
from flask import request

app = Flask("tipps_chur")

@app.route('/')
def tipps_chur():
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.
    return render_template("index.html")

@app.route('/neu')
def neue_idee():
    # Rendern des index.html Templates, für das Anzeigen der index.html Page.
    return render_template("neue_idee.html")



if __name__ == "__main__":
    app.run(debug=True, port=5001)

