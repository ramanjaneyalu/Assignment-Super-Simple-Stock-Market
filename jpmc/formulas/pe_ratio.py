from jpmc.formulas.geometric_mean import AbstractFormula


class PERatio(AbstractFormula):

    def __init__(self, price, dividend):
        self.__price = price
        self.__dividend = dividend

    def execute(self):
        return self.__price/self.__dividend

    def get_price(self):
        return self.__price

    def get_dividend(self):
        return self.__dividend
