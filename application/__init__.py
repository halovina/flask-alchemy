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
        from .homepage import route_api_blueprint
        app.register_blueprint(route_api_blueprint)
        
        from .userservice import user_api_blueprint
        app.register_blueprint(user_api_blueprint)
        
        from .uploadservice import upload_api_blueprint
        app.register_blueprint(upload_api_blueprint)
        
        from .blog import blog_api_blueprint
        app.register_blueprint(blog_api_blueprint)
        
        from .apitoken import apitoken_blueprint
        app.register_blueprint(apitoken_blueprint)
        
        from .balance import balance_blueprint
        app.register_blueprint(balance_blueprint)
        
        return app