import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

def create_app():
    
    environment_configiuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configiuration)
    
    db.init_app(app)
    
    with app.app_context():
        from . testratelimit import testratelimit_blueprint
        app.register_blueprint(testratelimit_blueprint)
        return app