from jpmc.formulas.geometric_mean import AbstractFormula


class VolumeWeightedStockPrice(AbstractFormula):
    def __init__(self, volume_weighted_stock_price, quantity):
        self.__volume_weighted_stock_price = volume_weighted_stock_price
        self.__quantity = quantity

    def execute(self):
        return self.__volume_weighted_stock_price / self.__quantity

    def get_volume_weighted_stock_price(self):
        return self.__volume_weighted_stock_price

    def get_quantity(self):
        return self.__quantity
