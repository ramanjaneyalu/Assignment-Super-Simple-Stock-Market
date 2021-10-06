# Assignment-Super-Simple-Stock-Market

## Project question

1. For a given stock,
	 1. Given any price as input, calculate the dividend yield
   1. Given any price as input, calculate the P/E Ratio
	 1. Record a trade, with timestamp, quantity, buy or sell indicator and price
	 1. Calculate Volume Weighted Stock Price based on trades in past 5 minutes
1. Calculate the GBCE All Share Index using the geometric mean of the Volume Weighted Stock Price for all
stocks

### Solution:

To run the code ```python app.py```

To run the test cases ```python unit_test.py```

There are 2 class for object creation,
1. Trade
1. Stock

There are 3 Enum types,

1. StockType (COMMON, PREFERRED)
1. TradeIndicator(BUY, SELL)
1. FormulaRequest(DividendYield, PERatio, GeometricMean, VolumeWeightedStockPrice)


###Solution description

1. app.py is the main class for this project. **StockEntityManager** manages all the operations that needs to be performed.
1. For Buy we check whether the symbol is valid or not, if it is valid then we store the trade in trade_store which will be used later for calculations.
1. **FormulaFactory** contains static methods(functions) which creates the specific formula object and returns it.
1. All the formula classes inhertis from the Abstract class **AbstractFormula** which has **execute** method and implements it.
1. Once the **StockEntityManager** gets the formula object by using the intermediate class **FormulaFactory** it executes it and returns the result.

Note: All the classes have members or variables as private and can be accessible using it' corresponding **get_variable_name** method to get the values.







   
