from enum import Enum
import datetime

from jpmc.formulas.common_dividend_yield import CommonDividendYield
from jpmc.formulas.geometric_mean import GeometricMean
from jpmc.formulas.pe_ratio import PERatio
from jpmc.formulas.preferred_dividend_yield import PreferredDividendYield
from jpmc.formulas.volume_weighted_stock_price import VolumeWeightedStockPrice
from jpmc.model.stock import StockType

FormulaRequest = Enum('FormulaRequest', 'DividendYield, PERatio, GeometricMean, VolumeWeightedStockPrice')


class FormulaFactory:

    @staticmethod
    def new_geometric_mean(exchange_data):
        formula = GeometricMean(exchange_data, len(exchange_data))
        return formula

    @staticmethod
    def new_pe_ratio(price, dividend):
        formula = PERatio(price, dividend)
        return formula

    @staticmethod
    def new_dividend_yield(price, stock):
        if stock.get_type() == StockType.COMMON:
            formula = CommonDividendYield(stock.get_last_dividend(), price)
        else:
            formula = PreferredDividendYield(stock.get_fixed_dividend(), stock.get_par_value(), price)

        return formula

    @staticmethod
    def new_volume_weighted_stock_price(trades, stock):
        last_five_minutes = int((datetime.datetime.now() - datetime.timedelta(minutes=5)).strftime("%H%M%S"))
        total = 0
        quantities = 0
        for trade in trades.keys():
            if trade[0] >= last_five_minutes:
                current_trade = trades[trade]
                if trades[trade].get_stock_symbol() == stock.get_stock_symbol():
                    total = current_trade.get_quantity() * current_trade.get_price()
                    quantities += current_trade.get_quantity()

        quantities = 1 if quantities == 0 else quantities

        formula = VolumeWeightedStockPrice(total, quantities)
        return formula
