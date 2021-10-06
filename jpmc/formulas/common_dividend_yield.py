from jpmc.formulas.geometric_mean import AbstractFormula


class CommonDividendYield(AbstractFormula):
    def __init__(self, last_dividend, price):
        self.__last_dividend = last_dividend
        self.__price = price

    @property
    def execute(self):
        return self.__last_dividend / self.__price

    def get_last_dividend(self):
        return self.__last_dividend

    def get_price(self):
        return self.__price
