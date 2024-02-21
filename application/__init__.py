import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import redis
from celery import Celery


db = SQLAlchemy()

dbredis = redis.Redis(decode_responses=True)

def create_app(**kwargs):
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    
    db.init_app(app)
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
        broker = 'redis://localhost:6379/0',
        backend = 'redis://localhost:6379/0',
        include=['application.celeryexample.tasks']
    )
    
celery = make_celery()