import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import redis

db = SQLAlchemy()

dbredis = redis.Redis(decode_responses=True)

def create_app():
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
        
        return app