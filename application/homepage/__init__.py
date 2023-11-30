from flask import Blueprint

route_api_blueprint = Blueprint('route_api', __name__)

from . import routes