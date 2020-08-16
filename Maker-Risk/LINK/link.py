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


# Binance concatenations
print(df_binance_linkbtc_hr[df_binance_linkbtc_hr.index.duplicated()].shape)
df_binance_linkbtc_hr = df_binance_linkbtc_hr.drop_duplicates()
print(df_binance_linkbtc_hr.shape)

print(df_binance_linketh_hr[df_binance_linketh_hr.index.duplicated()].shape)
df_binance_linketh_hr = df_binance_linketh_hr.drop_duplicates()
print(df_binance_linketh_hr.shape)

print(df_binance_linkusdc_hr[df_binance_linkusdc_hr.index.duplicated()].shape)
printdf_binance_linkusdc_hr= df_binance_linkusdc_hr.drop_duplicates()
print(df_binance_linkusdc_hr.shape)

print(df_binance_linkusdt_hr[df_binance_linkusdt_hr.index.duplicated()].shape)
df_binance_linkusdt_hr = df_binance_linkusdt_hr.drop_duplicates()
print(df_binance_linkusdt_hr.shape)

print(df_binanceus_linkusd_hr[df_binanceus_linkusd_hr.index.duplicated()].shape)
df_binanceus_linkusd_hr = df_binanceus_linkusd_hr.drop_duplicates()
print(df_binanceus_linkusd_hr)

print(df_binanceusa_linkusd_hr[df_binanceusa_linkusd_hr.index.duplicated()].shape)
df_binanceusa_linkusd_hr = df_binanceusa_linkusd_hr.drop_duplicates()
print(df_binanceusa_linkusd_hr.shape)

# Coinbase concatenations
print(df_coinbase_linkusd_hr[df_coinbase_linkusd_hr.index.duplicated()].shape)
df_coinbase_linkusd_hr = df_coinbase_linkusd_hr.drop_duplicates()
print(df_coinbase_linkusd_hr.shape)

print(df_coinbase_linketh_hr[df_coinbase_linketh_hr.index.duplicated()].shape)
df_coinbase_linketh_hr = df_coinbase_linketh_hr.drop_duplicates()
print(df_coinbase_linketh_hr.shape)

# Gemini concatenations
print(df_gemini_linkusd_hr[df_gemini_linkusd_hr.index.duplicated()].shape)
df_gemini_linkusd_hr = df_gemini_linkusd_hr.drop_duplicates()
print(df_gemini_linkusd_hr.shape)

print(df_gemini_linkbtc_hr[df_gemini_linkbtc_hr.index.duplicated()].shape)
df_gemini_linkbtc_hr = df_gemini_linkbtc_hr.drop_duplicates()
print(df_gemini_linkbtc_hr.shape)

# Kraken
print(df_kraken_linkbtc_hr[df_kraken_linkbtc_hr.index.duplicated()].shape)
df_kraken_linkbtc_hr = df_kraken_linkbtc_hr.drop_duplicates()
print(df_kraken_linkbtc_hr.shape)

print(df_kraken_linketh_hr[df_kraken_linketh_hr.index.duplicated()].shape)
df_kraken_linketh_hr = df_kraken_linketh_hr.drop_duplicates()
print(df_kraken_linketh_hr.shape)

print(df_kraken_linkusd_hr[df_kraken_linkusd_hr.index.duplicated()].shape)
df_kraken_linkusd_hr = df_kraken_linkusd_hr.drop_duplicates()
print(df_kraken_linkusd_hr.shape)

# Bittrex
print(df_bittrex_linkusdt_hr[df_bittrex_linkusdt_hr.index.duplicated()].shape)
df_bittrex_linkusdt_hr = df_bittrex_linkusdt_hr.drop_duplicates()
print(df_bittrex_linkusdt_hr.shape)

print(df_bittrex_linkbtc_hr[df_bittrex_linkbtc_hr.index.duplicated()].shape)
df_bittrex_linkbtc_hr = df_bittrex_linkbtc_hr.drop_duplicates()
print(df_bittrex_linkbtc_hr.shape)

print(df_bittrex_linketh_hr[df_bittrex_linketh_hr.index.duplicated()].shape)
df_bittrex_linketh_hr = df_bittrex_linketh_hr.drop_duplicates()
print(df_bittrex_linketh_hr)

# Poloniex
print(df_poloniex_linkusdt_hr[df_poloniex_linkusdt_hr.index.duplicated()].shape)
df_poloniex_linkusdt_hr = df_poloniex_linkusdt_hr.drop_duplicates()
print(df_poloniex_linkusdt_hr.shape)

print(df_poloniex_linkbtc_hr[df_poloniex_linkbtc_hr.index.duplicated()].shape)
df_poloniex_linkbtc_hr = df_poloniex_linkbtc_hr.drop_duplicates()
print(df_poloniex_linkbtc_hr.shape)

# Uniswap
print(df_uniswap_linketh_hr[df_uniswap_linketh_hr.index.duplicated()].shape)
df_uniswap_linketh_hr = df_uniswap_linketh_hr.drop_duplicates()
print(df_uniswap_linketh_hr.shape)