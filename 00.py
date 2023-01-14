import requests
from pprint import pprint

ur1 = 'https://api.bithumb.com/public/ticker/BTC_KRW'

r = requests.get(ur1).json()
print(r.get('data').get('closing_price'))