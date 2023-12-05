from flask import Blueprint, jsonify, request

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def index():
    try:
       # Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return "Ok {} {}".format(request.method, request.path)
    except Exception as ex:
        # Logger.add_to_log("error", str(ex))
        # Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': "Internal Server Error", 'success': False})
        return response, 500