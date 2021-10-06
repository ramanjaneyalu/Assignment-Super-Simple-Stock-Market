import datetime
import logging

from jpmc.model.trade import Trade, TradeIndicator
from jpmc.stock_data import StockData
from jpmc.exception import StockMarketException
from jpmc.formulas.formula_factory import FormulaFactory, FormulaRequest

logger = logging.getLogger(__name__)


class StockEntityManager:
    STOCK_PRICE_CHECK = 0.0

    def __init__(self):
        self.__trade_store = {}
        self.__stock_data = StockData().get_stock_list()

    def buy(self, stock_symbol, quantity, price):
        if stock_symbol in self.__stock_data.keys() and price > self.STOCK_PRICE_CHECK:
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            stock = self.__stock_data[stock_symbol]
            trade = Trade(stock, TradeIndicator.BUY, quantity, price)
            self.__trade_store[(int(timestamp), stock_symbol)] = trade
            logger.debug(f"Trade {trade} stored in memory trade store at time {int(timestamp)} (%H%M%S)")
            return str(trade)
        else:
            raise StockMarketException(f"Stock [" + stock_symbol + "] is not listed on the exchange.")

    def sell(self, stock_symbol, quantity, price):
        if stock_symbol in self.__stock_data.keys() and price > self.STOCK_PRICE_CHECK:
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            stock = self.__stock_data[stock_symbol]
            trade = Trade(stock, TradeIndicator.SELL, quantity, price)
            self.__trade_store[(int(timestamp), stock_symbol)] = trade
            logger.debug(f"Trade {trade} stored in memory trade store at time {int(timestamp)} (%H%M%S)")
            return str(trade)
        else:
            raise StockMarketException(f"Stock [" + stock_symbol + "] is not listed on the exchange.")

    def execute_formula_request(self, request, stock_symbol=None, price=None):
        if request == FormulaRequest.GeometricMean:
            formula_obj = FormulaFactory.new_geometric_mean(self.__trade_store)
            result = formula_obj.execute
            return result
        elif request in [FormulaRequest.PERatio, FormulaRequest.DividendYield,
                         FormulaRequest.VolumeWeightedStockPrice]:
            stock = self.__stock_data.get(stock_symbol)
            if request == FormulaRequest.PERatio and stock:
                formula_obj = FormulaFactory.new_pe_ratio(price, stock.get_last_dividend())
            elif request == FormulaRequest.DividendYield and stock:
                formula_obj = FormulaFactory.new_dividend_yield(price, stock)
            elif request == FormulaRequest.VolumeWeightedStockPrice and stock:
                formula_obj = FormulaFactory.new_volume_weighted_stock_price(self.__trade_store, stock)
            else:
                raise StockMarketException("Stock [" + stock_symbol + "] is not listed on the exchange.")
            result = formula_obj.execute
            return result
        else:
            raise StockMarketException(f"{request} **Not Supported**")
