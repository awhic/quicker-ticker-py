# Enter a stock ticker to get the most recent close price.

import pandas as pd
import requests

priceUnformatted: str
price: float

x = input()

ticker = ''
ticker = ticker + x
ticker = ticker.upper()

url_link = 'https://finance.yahoo.com/quote/' + ticker + '/history'


r = requests.get(url_link,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

data = pd.read_html(r.text)
data = data[0]
data = data['Close*']

pd.set_option('display.max_rows', 1)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

pricesList = data.values.tolist()
priceUnformatted = repr([pricesList[0]]).replace('[\'', '')
price = float(priceUnformatted.replace('\']', ''))

print(price)