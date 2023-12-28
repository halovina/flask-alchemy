from flask import Blueprint

apitoken_blueprint = Blueprint('apitoken', __name__)

from .import routes