from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=23091717, server="Deriv-Demo",password="yptod8tr"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

account_info=mt5.account_info()

if account_info!=None:
    # display trading account data 'as is'
    print(account_info)
    # display trading account data in the form of a dictionary
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
    print()
 
# display data on connection status, server name and trading account
print(mt5.terminal_info())
# display data on MetaTrader 5 version
print(mt5.version())

# obtenemos el número de todas las órdenes en la historia
from_date=datetime(2020,1,1)
to_date=datetime.now()
history_orders=mt5.history_orders_total(from_date, datetime.now())
if history_orders>0:
    print("Total history orders=",history_orders)
else:
    print("Orders not found in history")

# obtenemos el número de transacciones en la historia
from_date=datetime(2020,1,1)
to_date=datetime.now()
deals=mt5.history_deals_get(from_date, to_date)
print("Total deals=",deals)
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()