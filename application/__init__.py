import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    environment_configiuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configiuration)
    
    db.init_app(app)
    Session(app)
    
    with app.app_context():
        from .redissession import redis_session_blueprint
        app.register_blueprint(redis_session_blueprint)
        
        return app