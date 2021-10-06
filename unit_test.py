import unittest

from jpmc.formulas.common_dividend_yield import CommonDividendYield
from jpmc.formulas.formula_factory import FormulaRequest
from jpmc.formulas.pe_ratio import PERatio
from jpmc.formulas.preferred_dividend_yield import PreferredDividendYield
from jpmc.stock_data import StockData
from jpmc.stock_entity_manager import StockEntityManager


class UnitTests(unittest.TestCase):

    def setUp(self) -> None:
        self.stock_data = StockData().get_stock_list()
        self.stock_entity_manager_obj = StockEntityManager()

    def test_check_pe_ratio(self):
        stock = self.stock_data.get("ALE")
        result = self.stock_entity_manager_obj.execute_formula_request(FormulaRequest.PERatio, "ALE", 85)
        pe_ratio_obj = PERatio(85, stock.get_last_dividend())
        expected_result = pe_ratio_obj.execute()
        self.assertEqual(result, expected_result)

    def test_dividend_yield_common(self):
        stock = self.stock_data.get("ALE")
        result = self.stock_entity_manager_obj.execute_formula_request(FormulaRequest.DividendYield, "ALE", 185)
        dividend_yield_obj = CommonDividendYield(stock.get_last_dividend(), 185)
        expected_result = dividend_yield_obj.execute()
        self.assertEqual(result, expected_result)

    def test_dividend_yield_preferred(self):
        stock = self.stock_data.get("GIN")
        result = self.stock_entity_manager_obj.execute_formula_request(FormulaRequest.DividendYield, "GIN", 185)
        dividend_yield_obj = PreferredDividendYield(stock.get_fixed_dividend(), stock.get_par_value(), 185)
        expected_result = dividend_yield_obj.execute()
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
