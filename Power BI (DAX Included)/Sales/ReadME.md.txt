DAX Used

Sales = SUM(Sales_Data[Sales])

Prev_Year_Sales = CALCULATE([Sales],SAMEPERIODLASTYEAR('DAX DateTable'[Date]))

Sales vs PY = [Sales]-[Prev_Year_Sales] 

Sales vs PY% = [Sales vs PY]/[Sales]

Profit = SUM(Sales_Data[Profit])

Profit LY = CALCULATE([Profit],SAMEPERIODLASTYEAR('DAX DateTable'[Date]))

Profit Margin = DIVIDE([Profit],[Sales],0)

Profit vs LY% = [Profit vs Profit LY]/[Profit]

Profit vs Profit LY = [Profit]-[Profit LY]

Products Sold = SUM(Sales_Data[Order Quantity])

Total Cost = SUM(Sales_Data[Total Cost])