from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    rexturn "Hello, flask from 13512043!"
