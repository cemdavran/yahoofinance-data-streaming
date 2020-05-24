# Yahoo finance data streaming with aws lambda
I used yfinance module to get the pricing imformation of stocks below:

  [Facebook (FB), Shopify (SHOP), Beyond Meat (BYND), Netflix (NFLX), Pinterest (PINS), Square (SQ, The Trade Desk(TTD)
  Okta (OKTA), Snap (SNAP), Datadog (DDOG]

- One-day(May 14th 2020) of high and low stock prices were pulled for each of those 10 company at an one minute interval.
- AWS lambda function(Data Collector) created to collect the stock data, transformed into a JSON format 
  and transformed  records were put into a firehose delivery stream to transferred into S3 bucket.

Lambda Function [URL](https://we83os9z5g.execute-api.us-east-2.amazonaws.com/default/yfinance-collector): https://we83os9z5g.execute-api.us-east-2.amazonaws.com/default/yfinance-collector
