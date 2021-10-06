from jpmc.formulas.geometric_mean import AbstractFormula


class PreferredDividendYield(AbstractFormula):
    def __init__(self, fixed_dividend, par_value, price):
        self.__fixed_dividend = fixed_dividend
        self.__par_value = par_value
        self.__price = price

    @property
    def execute(self):
        return (self.__fixed_dividend * self.__par_value) / self.__price

    def get_fixed_dividend(self):
        return self.__fixed_dividend

    def get_par_value(self):
        return self.__par_value

    def get_price(self):
        return self.__price
