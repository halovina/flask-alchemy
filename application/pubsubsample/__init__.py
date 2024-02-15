from flask import Blueprint

pubsub_blueprint = Blueprint('pubsub_blueprint', __name__)

from . import routes