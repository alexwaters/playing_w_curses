import api
import config, json, time
from urllib import urlopen

client_key = config.client_key
secret_key = config.client_password
userId = config.user_id

#create the api connection
itbit_api_conn = api.itBitApiConnection(clientKey=client_key, secret=secret_key, userId=userId)

def main():
    #Get order book
    order_book = itbit_api_conn.get_order_book('XBTUSD').json()

    #get all the wallets for the user
    #wallets = itbit_api_conn.get_all_wallets().json()

    #get the id of the wallet named Wallet
    #walletId = next(wallet for wallet in wallets if wallet['name'] == 'Wallet')['id']

    #print the trades for the selected wallet
    #print(json.dumps(itbit_api_conn.get_wallet_trades(walletId).json(), indent=2))

    print(json.dumps(order_book, indent=4))

def get_price(pair):
    return json.dumps(itbit_api_conn.get_ticker(pair).json())

def get_averages(num=10, pairs=['XBTUSD', 'XBTEUR', 'XBTSGD']):
    if isinstance(num, int):
        avgs = []
        for pair in pairs:
            data = json.loads(urlopen("https://api.itbit.com/v1/markets/%s/trades" % pair).read())['recentTrades'][:num]
            total = 0
            for item in data:
                total += float(item['price'])
            avgs.append(round(total/num,2))
        avg_prices = dict(zip(pairs,avgs))
    return avg_prices
