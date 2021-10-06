import logging

from jpmc.stock_entity_manager import StockEntityManager
from jpmc.formulas.formula_factory import FormulaRequest

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def main():
    try:
        stock_entity_manager_obj = StockEntityManager()
        trade_result = stock_entity_manager_obj.buy("POP", 100, 10)
        logger.debug(trade_result)
        trade_result = stock_entity_manager_obj.sell("JOE", 4, 1000)
        logger.debug(trade_result)
        result = stock_entity_manager_obj.execute_formula_request(FormulaRequest.GeometricMean)
        logger.debug(f"The GBCE All Share Index using the geometric mean of prices for all stocks = {result}")
        result = stock_entity_manager_obj.execute_formula_request(FormulaRequest.PERatio, "ALE", 85)
        logger.debug(f"PERatio result = {result}")
        # dividend yield for preferred
        result = stock_entity_manager_obj.execute_formula_request(FormulaRequest.DividendYield, "GIN", 185)
        logger.debug(f"DividendYield for preferred, result = {result}")
        result = stock_entity_manager_obj.execute_formula_request(FormulaRequest.DividendYield, "ALE", 185)
        logger.debug(f"DividendYield for common, result = {result}")
        result = stock_entity_manager_obj.execute_formula_request(FormulaRequest.VolumeWeightedStockPrice, "POP")
        logger.debug(f"VolumeWeightedStockPrice for symbol selected(POP), result = {result}")
    except Exception as e:
        print("exception occurred", e)


if __name__ == "__main__":
    main()
