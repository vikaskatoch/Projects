DAX used

CY Sales = 

Var CY = MAX('Date Table'[Year])

RETURN
CALCULATE(SUM(Sales[Sale Amount]),'Date Table'[Year]=CY)


PY Sales = CALCULATE([CY Sales],SAMEPERIODLASTYEAR('Date Table'[Date]))

YoY Sales Growth% = DIVIDE([CY Sales]-[PY Sales],[PY Sales])

Budgeted Sales = 
VAR CY = MAX('Date Table'[Year])

RETURN
CALCULATE(SUM(Budget[Budgeted Amt]),'Date Table'[Year]=CY)

Budgeted Variance = DIVIDE([CY Sales]-Budget[Budgeted Sales],Budget[Budgeted Sales])