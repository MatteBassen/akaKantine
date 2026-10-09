from flask import Flask, render_template

app = Flask(__name__)

#Ruten til hjemmesiden
@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
