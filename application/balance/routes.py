from .import balance_blueprint
from flask import jsonify, make_response
from application.apitoken.common import validate_signature_service

@balance_blueprint.route('/api/v1/balance-inquiry', methods=['POST'])
@validate_signature_service
def api_balance_inquiry():
    return make_response(
        jsonify({
            'message':'inquiry balance success'
        }), 200
    )