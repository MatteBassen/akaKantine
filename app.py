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

if __name__ == '__main__':
    app.run()
