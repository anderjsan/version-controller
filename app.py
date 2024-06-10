# app.py
from flask import Flask
from updater.updater import Updater

if __name__ == "__main__":
    app = Flask(__name__)
    updater = Updater(app)
    updater.run()