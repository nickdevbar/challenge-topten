from datetime import datetime
import MetaTrader5 as mt5

from src.models.metaTrader5 import MetaTrader5


class MetaTraderService():

    @classmethod
    def get_data(cls, login, password):
        try:
            if not mt5.initialize(login=login, server="Deriv-Demo", password = password):
                print("initialize() failed, error code =", mt5.last_error())
                quit()
           
            #example = datetime.fromisoformat(str(data.from_date)) # data.from_date
            from_date = datetime(2020,1,1)
            #print('ejemplos de fechas: ', from_date, example)
            to_date = datetime.now() # data.to_date

            deals = mt5.history_deals_get(from_date, to_date) # consulta al mt5
            array = []
            for deal in deals:
                dealObj = MetaTrader5(
                    deal.ticket, deal.order, deal.time,
                    deal.position_id, deal.volume, deal.price,
                    deal.profit, deal.symbol
                )
                array.append(dealObj.to_json())
            return array
        except Exception as ex:
            print('error en metaTraderService...')