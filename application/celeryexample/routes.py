from .tasks import print_messages
from . import celery_blueprint
from flask import jsonify

@celery_blueprint.route('/celery/test-message', methods=['GET'])
def publish_message():
    print_messages.delay(str_message="test background process")
    return jsonify(
        {
            'message':'data Anda sedang di proses'
        }
    )