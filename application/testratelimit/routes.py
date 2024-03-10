from . import testratelimit_blueprint
from flask import make_response, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from application import app


limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


@testratelimit_blueprint.route('/ratelimit/test-rate-limit', methods=['GET'])
@limiter.limit('1/minute')
def test_rate_limit():
    return make_response(
        jsonify(
            {
                'message':'success'
            }
        )
    )