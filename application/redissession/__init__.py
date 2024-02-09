from flask import Blueprint

redis_session_blueprint = Blueprint('redis_session_blueprint', __name__)

from . import routes