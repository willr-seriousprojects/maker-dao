import requests
from pandas.io.json import json_normalize
import pandas as pd 
import json

url = "https://api.coingecko.com/api/v3/coins/link/market_chart/range?vs_currency=usd&from=1546300800&to=1577836800"
# get data from endpoint and load json content
resp = requests.get(url)
# parse json into py dict
resp = json.loads(resp.content)

# set df from json dict
# use list comprehension to iterate
df = pd.DataFrame({
    'dates':[x[0] for x in resp['prices']],
    'prices': [x[1] for x in resp['prices']],
    'market_caps': [x[1] for x in resp['market_caps']],
    'total_volumes': [x[1] for x in resp['total_volumes']]
})
# change date format
df['dates'] = pd.to_datetime(df['dates'], unit='ms')
# set df index to date
df.set_index('dates', inplace=True)
print(df.head())