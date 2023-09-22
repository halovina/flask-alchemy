import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        from .userservice import user_api_blueprint
        app.register_blueprint(user_api_blueprint)
        return app