from flask import Flask
from updater.updater import Updater
from updater.app_swagger import App_swagger

if __name__ == "__main__":
    app = Flask(__name__)
    updater = Updater(app)
    swg = App_swagger(app)
    
    updater.run(port=4006)