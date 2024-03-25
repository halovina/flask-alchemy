from .tasks import print_message
from . import celery_blueprint
from flask import jsonify

@celery_blueprint.route('/celery/test-message', methods=['GET'])
def publish_message():
    print_message.delay("test backgroud processss")
    return jsonify(
        {
            'message':' data Anda sedang di proses'
        }
    )