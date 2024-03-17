import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    if environment_configuration == 'production':
        app.config.from_object(ProductionConfig)
    elif environment_configuration == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.logger.info('FLASK_ENV is NULL !!')
    
    db.init_app(app)
    
    with app.app_context():
        return app