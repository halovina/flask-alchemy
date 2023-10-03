from flask import Blueprint

upload_api_blueprint = Blueprint('upload_api', __name__)

from . import routes