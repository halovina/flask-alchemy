import os
import pytest 
from application.models import User

from application import create_app, db

@pytest.fixture
def tclient():
    
    os.environ['CONFIGURATION_SETUP'] = 'config.DevelopmentConfig'
    os.environ['SECRET_KEY'] = '1233434345'
    
    flask_app = create_app()
    
    with flask_app.test_client() as tclient:
        with flask_app.app_context():
            yield tclient
        
        
@pytest.fixture      
def init_mock_userdata(tclient):
    
    user_1 = User(
        username = "user1_test",
        email = "user1_test@gmail.com",
        first_name = "user1 firstname",
        last_name = "user1 lastname",
        password = "user-123456"
    )
    user_2 = User(
        username = "user2_test",
        email = "user2_test@gmail.com",
        first_name = "user2 firstname",
        last_name = "user2 lastname",
        password = "user-123456"
    )
    
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()
    
    yield #this is where the testing happens
    
    db.session.delete(user_1)
    db.session.delete(user_2)
    db.session.commit()