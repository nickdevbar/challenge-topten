from flask import Blueprint, request, jsonify

from src.services.MetaTraderService import MetaTraderService

main = Blueprint('metatrader_blueprint', __name__) # --> par uso de las rutas


@main.route('/historiales')
def get_languages():
    
    login = request.args.get('login', type=int), # return tuple = ('xxxxxxxx',) type=int para convertir en entero: (xxxxxxxx,)
    password = request.args.get('password')
    try:
        deals = MetaTraderService.get_data(login[0], password)

        if (len(deals) > 0):
            return jsonify({'deals': deals, 'success': True})
        else:
            return jsonify({'message': "NOT FOUND (sin historial)", 'success': True})
    except Exception as ex:
        # Logger.add_to_log("error", str(ex))
        # Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False}), 404