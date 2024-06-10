# app_swg.py
from flask import Flask
from updater.updater import Updater
from updater.app_swagger import AppSwagger

def initialize_app():
    app = Flask(__name__)
    updater = Updater(app)
    swg = AppSwagger(app)
    
    swg.run()
    updater.run()

if __name__ == "__main__":
    initialize_app()