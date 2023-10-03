from . import upload_api_blueprint
from flask import request, make_response, jsonify
from werkzeug.utils import secure_filename


@upload_api_blueprint.route('/upload/file', methods=['POST'])
def upload_file():
    try:
        file = request.files['myfile']
        file.save("./uploads/{}".format(secure_filename(file.filename)))
        
        return make_response(
            jsonify({
                'message':'success'
            }), 200
        )
    except Exception as e:
        return make_response(
            jsonify({
                'message': str(e)
            }), 400
        )
    
    