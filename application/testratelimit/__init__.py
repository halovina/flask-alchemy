from flask import Blueprint

testratelimit_blueprint = Blueprint('testratelimit_blueprint', __name__)

from . import routes