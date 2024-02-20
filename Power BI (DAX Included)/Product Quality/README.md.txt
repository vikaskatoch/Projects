DAX Used

Defects% = DIVIDE(SUM('Quality Data'[Defects]),SUM('Quality Data'[Total Task]))

Fatal Error% = DIVIDE(SUM('Quality Data'[Fatel Errors]),SUM('Quality Data'[Total Task]))

Quality Score = IF([Defects%]=BLANK(),BLANK(),1-[Defects%])

Sampling% = DIVIDE(SUM('Quality Data'[Samples]),SUM('Quality Data'[Total Task]))