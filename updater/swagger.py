import os
from flask import json
from flask_swagger_ui import get_swaggerui_blueprint

class App_swagger:
    def __init__(self, app):
        self.app = app
        self.SWAGGER_URL = '/swagger'
        self.API_URL = '/static/swagger.json'  # Updated path
        self.bp = get_swaggerui_blueprint(
            self.SWAGGER_URL,
            self.API_URL,
            config={
                'app_name': "API TAG Controller",
                'description':'AJS Consulting',
                'version':'0.4.0',
                'termsOfServiceUrl':'Not Applicable',
                'contact':{
                    'name':'Anderson',
                    'url':'https://ajsconsulting.com',
                    'email':'ajs@ajsconsulting.com',
                    'linkedin':'https://linkedin.com/in/anderjsan'
                }
            }
        )
        self.app.register_blueprint(self.bp, url_prefix=self.SWAGGER_URL)
        self.app.config['SWAGGER_JSON'] = self.API_URL

    def get_swagger_json(self):
        with open(os.path.join(os.path.dirname(__file__), 'static', 'swagger.json')) as f:
            return json.load(f)
