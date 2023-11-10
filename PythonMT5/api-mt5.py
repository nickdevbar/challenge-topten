# API
from flask import Flask, jsonify
from flask_cors import CORS

# MetaTrader 5
from datetime import datetime
import MetaTrader5 as mt5

# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=23091717, server="Deriv-Demo",password="yptod8tr"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

account_info=mt5.account_info()

if account_info!=None:
    # display trading account data 'as is'
    #print(account_info)
    # display trading account data in the form of a dictionary
    #print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    #for prop in account_info_dict:
        #print("  {}={}".format(prop, account_info_dict[prop]))
    #print()
 
# display data on connection status, server name and trading account
#print(mt5.terminal_info())
# display data on MetaTrader 5 version
#print(mt5.version())

# obtenemos el número de transacciones en la historia
from_date=datetime(2020,1,1)
to_date=datetime.now()
deals=mt5.history_deals_get(from_date, to_date)
print("Total deals=",deals)
# Ruta de ejemplo

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/historiales')
def todas_las_transacciones():
    return jsonify(message=deals)

# Ruta de ejemplo
@app.route('/')
def hello_world():
    return jsonify(message='Hola, esta es tu API con Flask')

# Otra ruta de ejemplo
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return jsonify(saludo=f'Hola, {nombre}!')

if __name__ == '__main__':
    app.run(debug=True)
