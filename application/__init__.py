import os
from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from celery import Celery


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    if environment_configuration == 'development':
        app.config.from_object(DevelopmentConfig)
    elif environment_configuration == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.logger.info('FLASK_ENV is Null ..!')
    
    
    with app.app_context():
        
        from .celeryexample import celery_blueprint
        app.register_blueprint(celery_blueprint)
        
        return app
    
def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker= os.environ['CELERY_BROKER_URL'],
        backend= os.environ['CELERY_RESULT_BACKEND'],
        include=['application.celeryexample.tasks']
    )
    
celery = make_celery()