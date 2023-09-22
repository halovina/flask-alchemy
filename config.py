import os 
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
    
class Config:
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig:
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost/flask-alchemy'
    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.environ['SECRET_KEY']
    

class ProductionConfig:
    ENV = "production"
    DEBUG = True
    SQLALCHEMY_DATABSE_URI = 'mysql+pymysql://admin:admin@localhost/flask-alchemy'
    SQLALCHEMY_ECHO = True