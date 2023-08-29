import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    environment_configiuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configiuration)
    
    db.init_app(app)
    
    with app.app_context():
        return app