from flask import Blueprint

blog_api_blueprint = Blueprint('blog_api', __name__)

from . import routes