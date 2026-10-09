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
def drikkevare(vare_id):
    for vare in drikkevarer + matvarer:
        if vare_id == vare['id']:
            return render_template("visVare.html", vare = vare)
    return """
        <h1>Vi har ikke denne varen</h1>
        <a href='/varer'>tilbake til alle varer</a>   
    """


if __name__ == '__main__':
    app.run(debug = True)
