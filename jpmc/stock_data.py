from jpmc.model.stock import Stock, StockType


class StockData:
    _stock_list = {
        "TEA": Stock("TEA", StockType.COMMON, 0.0, 0.0, 100.0),
        "POP": Stock("POP", StockType.COMMON, 8.0, 0.0, 100.0),
        "ALE": Stock("ALE", StockType.COMMON, 23.0, 0.0, 60.0),
        "GIN": Stock("GIN", StockType.PREFERRED, 8.0, 0.2, 100.0),
        "JOE": Stock("JOE", StockType.COMMON, 13.0, 0.0, 250.0)
    }

    def get_stock_list(self):
        return self._stock_list

