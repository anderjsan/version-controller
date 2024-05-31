from flask import jsonify, json
from flask_swagger_ui import get_swaggerui_blueprint
import os

class appSwagger:
    def __init__(self):
        self.SWAGGER_URL = '/swagger'
        self.API_URL = '/static/swagger.json'
        self.swagger_bp = get_swaggerui_blueprint(
            self.SWAGGER_URL,
            self.API_URL,
            config= {
                'app_name': "API TAG Controller",
                'description': 'API that generates new TAG For Docker Version. Works along with Jenkins.',
                'version': '3.7.0',
                'Terms of Service': 'Not Applicable',
                'contact':{
                    'name': 'Anderson Santos',
                    'email': 'anderjsan@gmail.com',
                    'linkedin': 'https://www.linkedin.com/in/anderjsan/'
                }
            }
        )
    
    def generate_swagger_json(self, app):
        # Generate the swagger.json file from the app
        with app.app_context():
            swag = app.swagger.to_dict()
            script_dir = os.path.dirname(os.path.realpath(__file__))
            swagger_file_path = os.path.join(script_dir, 'static', 'swagger.json')
            with open(swagger_file_path, 'w') as file:
                json.dump(swag, file, indent=2)

    def swagger_json(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        swagger_file_path = os.path.join(script_dir, 'static', 'swagger.json')
        with open(swagger_file_path, 'r') as file:
            swagger_json = file.read()
            return jsonify(json.loads(swagger_json))
    
    def generate_swagger_json(self, app):
        # Generate the swagger.json file from the app
        with app.app_context():
            swag = app.swagger.to_dict()
            script_dir = os.path.dirname(os.path.realpath(__file__))
            swagger_file_path = os.path.join(script_dir, 'static', 'swagger.json')
            with open(swagger_file_path, 'w') as file:
                json.dump(swag, file, indent=2)