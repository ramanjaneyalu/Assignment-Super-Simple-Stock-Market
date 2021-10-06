from enum import Enum

TradeIndicator = Enum('TradeIndicator', 'BUY, SELL')


class Trade:
    __type = None
    __quantity = 0
    __price = 0.0

    def __init__(self, stock, trade_type, quantity, price):
        self.__stock = stock
        self.__trade_type = trade_type
        self.__quantity = quantity
        self.__price = price

    def get_type(self):
        return self.__type

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def get_stock_symbol(self):
        return self.__stock.get_stock_symbol()

    def __str__(self):
        return "Trade stock="+str(self.__stock.get_stock_symbol())+" [type=" + str(self.__trade_type) + \
               ", quantity=" + str(self.__quantity) + ", price=" + \
               str(self.__price) + "]"
