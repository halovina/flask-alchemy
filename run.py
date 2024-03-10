from application import create_app
from flask import make_response, jsonify

app = create_app()

@app.route('/')
def hello():
    return 'hello world'

@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
        jsonify(
            {
                'message':'ratelimit : {}'.format(e.description)
            }
        ), 429
    )

if __name__ == '__main__':
    app.run()