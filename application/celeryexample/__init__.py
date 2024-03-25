from flask import Blueprint


celery_blueprint = Blueprint('celery_blueprint', __name__)

from . import routes