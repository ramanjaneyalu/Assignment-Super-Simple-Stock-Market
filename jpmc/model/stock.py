from enum import Enum

StockType = Enum('StockType', 'COMMON, PREFERRED')


class Stock:
    __stock_type = StockType.COMMON

    def __init__(self, stock_symbol, stock_type, last_dividend, fixed_dividend, par_value):
        self.__stock_symbol = stock_symbol
        self.__stock_type = stock_type
        self.__last_dividend = last_dividend
        self.__fixed_dividend = fixed_dividend
        self.__par_value = par_value

    def get_stock_symbol(self):
        return self.__stock_symbol

    def set_stock_symbol(self, stock_symbol):
        self.__stock_symbol = stock_symbol

    def get_par_value(self):
        return self.__par_value

    def set_par_value(self, par_value):
        self.__par_value = par_value

    def get_type(self):
        return self.__stock_type

    def set_type(self, stock_type):
        self.__stock_type = stock_type

    def get_last_dividend(self):
        return self.__last_dividend

    def set_last_dividend(self, last_dividend):
        self.__last_dividend = last_dividend

    def get_fixed_dividend(self):
        return self.__fixed_dividend

    def set_fixed_dividend(self, fixed_dividend):
        self.__fixed_dividend = fixed_dividend

    def __str__(self):
        return "Stock [ Stock Symbol = " + self.__stock_symbol + ", Type = " + self.__stock_type + ", Last Dividend = " + \
               self.__last_dividend + ", Fixed Dividend = " + self.__fixed_dividend + ", Par Value = " + \
               self.__par_value + " ]"
