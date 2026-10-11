from flask import Flask, render_template
from data import ukesmat, drikkevarer, matvarer

app = Flask(__name__)

#Ruten til hjemmesiden
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/varer')
def varer():
    return render_template("varer.html", drikkevarer = drikkevarer, matvarer = matvarer )

@app.route('/vare/<int:vare_id>')
def visVare(vare_id):
    for vare in drikkevarer + matvarer:
        if vare_id == vare['id']:
            return render_template("visVare.html", vare = vare, drikkevarer = drikkevarer, matvarer = matvarer)
    return """
        <h1>Vi har ikke denne varen</h1>
        <a href='/varer'>tilbake til alle varer</a>   
    """

@app.route('/ukesMeny')
def ukesMeny():
    return render_template("ukesMeny.html", ukesmeny = ukesmat)


@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")


if __name__ == '__main__':
    app.run(debug = True)
