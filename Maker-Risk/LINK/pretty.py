import json
import requests
import pandas as pd



# url = "https://api.aleth.io/v0/defi/history"

# resp = requests.get(url, params={
#     # 'periods': '3600',
#     # 'after': str(int(pd.Timestamp(after).timestamp()))
#     'after': '1596153600',
#     'assets':['link'],
#     # 'metrics': ['earn_apr','borrow_apr'],
#     # 'protocols': ['aave']	
# })
# resp = json.loads(resp.content)
# PrettyJson = json.dumps(resp, indent=4, separators=(',', ': '), sort_keys=True)
# print(PrettyJson)


# url = "https://api.aleth.io/v0/defi/stats"

# resp = requests.get(url, params={
#     # 'periods': '3600',
#     # 'after': str(int(pd.Timestamp(after).timestamp()))
#     'after': '1596585600',
#     'assets':['link'],
#     # 'metrics': ['supply_volume'],
#     'protocols': ['aave']	
# })
# resp = json.loads(resp.content)
# PrettyJson = json.dumps(resp, indent=4, separators=(',', ': '), sort_keys=True)
# print(PrettyJson)

# url = "https://min-api.cryptocompare.com/data/v2/pair/mapping/exchange/fsym?exchangeFsym=HOLO&api_key=83e625a6bc3dbda445bd3b9001ba7d6f63ffafc91f75763f4a9b993bb1e2514d"
# resp = requests.get(url)
# resp = json.loads(resp.content)
# PrettyJson = json.dumps(resp, indent=4, separators=(',', ': '), sort_keys=True)
# print(PrettyJson)

# # 83e625a6bc3dbda445bd3b9001ba7d6f63ffafc91f75763f4a9b993bb1e2514d

# url = 'https://data.messari.io/api/v1/assets/metrics'
# # url = 'https://data.messari.io/api/v1/assets/chainlink/metrics/real.vol/time-series'
# resp = requests.get(url)
# resp = json.loads(resp.content)
# PrettyJson = json.dumps(resp, indent=4, separators=(',', ': '), sort_keys=True)
# print(PrettyJson)

# timeframe='day'
# start='2020-07-29' 
# end='2020-07-31'
# url = 'https://api.bancor.network/0.1/currencies/volumeHistory?'
# resp = requests.get(url, params={
#     'toCurrencyCode': 'LINK',
#     'fromCurrencyCode': 'ETH',
#     'timeFrame': f'{timeframe}',
#     'startDate': str(int(pd.Timestamp(start).timestamp())),
#     'endDate': str(int(pd.Timestamp(end).timestamp()))

# })
# resp = json.loads(resp.content)
# PrettyJson = json.dumps(resp, indent=4, separators=(',', ': '), sort_keys=True)
# print(PrettyJson)


url = 'https://api.bancor.network/0.1/currencies/volumeHistory?toCurrencyCode=link&fromCurrencyCode=eth&timeFrame=week'
resp = requests.get(url)
resp = json.loads(resp.content)
PrettyJson = json.dumps(resp, indent=4, separators=(',', ': '), sort_keys=True)
print(PrettyJson)