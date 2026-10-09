from flask import Flask, render_template
from data import ukesmat, varer

app = Flask(__name__)

#Ruten til hjemmesiden
@app.route('/')
def index():
    return render_template("index.html", varer = varer)


if __name__ == '__main__':
    app.run()
