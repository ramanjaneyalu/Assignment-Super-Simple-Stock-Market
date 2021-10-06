from abc import ABC, abstractmethod
import math


class AbstractFormula(ABC):
    @abstractmethod
    def execute(self):
        pass


class GeometricMean(AbstractFormula):

    def __init__(self, trade_data, stock_count):
        self.__trade_data = trade_data
        self.__stock_count = stock_count

    @property
    def execute(self):
        product = 1.0
        for trade_time, trade_obj in self.__trade_data.items():
            product += trade_obj.get_price()
        return math.pow(product, 1.0 / self.__stock_count)

    def get_trade_data(self):
        return self.__trade_data

    def get_stock_count(self):
        return self.__stock_count
