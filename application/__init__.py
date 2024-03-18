import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import redis
from celery import Celery
from config import DevelopmentConfig, ProductionConfig


# db = SQLAlchemy()

dbredis = redis.Redis(decode_responses=True)

def create_app(**kwargs):
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    if environment_configuration == 'develoment':
        app.config.from_object(DevelopmentConfig)
    elif environment_configuration == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.logger.info('FLASK_ENV is NULL !!')
    
    # db.init_app(app)
    Session(app)
    
    with app.app_context():
        from .redissession import redis_session_blueprint
        app.register_blueprint(redis_session_blueprint)
        
        from .pubsubsample import pubsub_blueprint
        app.register_blueprint(pubsub_blueprint)
        
        from .celeryexample import celery_blueprint
        app.register_blueprint(celery_blueprint)
        
        return app
    

def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker = os.environ['CELERY_BROKER_URL'],
        backend = os.environ['CELERY_RESULT_BACKEND'],
        include=['application.celeryexample.tasks']
    )
    
celery = make_celery()