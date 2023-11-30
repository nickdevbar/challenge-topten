class MetaTrader5():

    def __init__(self, ticket, order, time, position_id, volume, price, profit, symbol) -> None:
        self.ticket = ticket
        self.order = order
        self.time = time
        self.position_id = position_id
        self.volume = volume
        self.price = price
        self.profit = profit
        self.symbol = symbol

    def to_json(self):
        return {
            'ticket': self.ticket,
            'order': self.order,
            'time': self.time,
            'position_id': self.position_id,
            'volume': self.volume,
            'price': self.price,
            'profit': self.profit,
            'symbol': self.symbol
        }