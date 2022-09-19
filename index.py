from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>Flask Vercel</h2>"

@app.route("/next")
def next():
    return "<h2>Flask next Vercel</h2>"
