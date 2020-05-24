import boto3
import os
import subprocess
import sys
import json

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance as yf

def lambda_handler(event, context):
    ticks = "FB SHOP BYND NFLX PINS SQ TTD OKTA SNAP DDOG"
    tickList = ticks.split()
    data = yf.download(ticks, start="2020-05-14", end="2020-05-15", interval = "1m",group_by = 'ticker')
    # initialize boto3 client
    fh = boto3.client("firehose", "us-east-2")
    
    
    for i in tickList:
        for index, rows in data[i].iterrows():
            jsonstr = json.dumps({"high": rows.High, "low": rows.Low, "ts": str(index), 'name': i})
            
           
            fh.put_record(DeliveryStreamName="YFinance-DataStreaming", Record={"Data": jsonstr.encode('utf-8')})

    return {'statusCode': 200,'body': json.dumps(f'Completed! Data Recorded into your bucket')}