import time
from random import seed
from random import randint
seed(2)
txMax = 5
#  MarketData
from kucoin.client import Market
market = Market(url='https://api.kucoin.com')
#market = Market()

# or connect to Sandbox
#market = Market(url='https://openapi-sandbox.kucoin.com')
#market = Market(is_sandbox=True)
api_key = ''
api_secret = ''
def returnBid(symbol):
    book = market.get_aggregated_order(symbol)
    return book['bids'][1][0]
# User
from kucoin.client import User
user = User(api_key, api_secret, api_passphrase)

# or connect to Sandbox
#user = User(api_key, api_secret, api_passphrase, is_sandbox=True)

def returnAccountAvailable(token):
    account = user.get_account_list(token, "trade")
    return account[0]['available']
def returnPrice(token):
    account = market.get_ticker(token)
    return account['price']
# Trade
from kucoin.client import Trade
client = Trade(api_key, api_secret, api_passphrase)

# or connect to Sandbox
# client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)# Trade


while(1):
     available = returnAccountAvailable('USDT')
     debut = time.time()
     bid = returnBid('BTC-USDT')
     try:
         order = client.create_limit_order('BTC-USDT', 'sell', randint(1,txMax), bid)
         print(order)
         fin = time.time()
         print(fin - debut)
         time.sleep(randint(10, 120))
     except Exception as err:
         print(err)
         break