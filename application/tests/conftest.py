import os
import pytest 

from application import create_app

@pytest.fixture
def tclient():
    
    os.environ['CONFIGURATION_SETUP'] = 'config.DevelopmentConfig'
    os.environ['SECRET_KEY'] = '1233434345'
    
    flask_app = create_app()
    
    with flask_app.test_client() as tclient:
        yield tclient