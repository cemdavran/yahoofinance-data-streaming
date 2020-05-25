SELECT name as CompanyName, substring(ts,12,2) as Hour, high as HighestPrice, substring(ts,1,19) as HighestOccured


FROM (SELECT name as Company, substring(ts,12,2) as hour1, MAX(high) as highprice 
      FROM yahoo_finance_data GROUP BY name, substring(ts,12,2)) 

firsttable 
JOIN 
(SELECT name, substring(ts,12,2) as hour2, high,ts FROM yahoo_finance_data) 
secondtable 

ON 
firsttable.Company = secondtable.name 
AND firsttable.hour1 =secondtable.hour2 
AND firsttable.highprice = secondtable.high

ORDER BY CompanyName, Hour;
