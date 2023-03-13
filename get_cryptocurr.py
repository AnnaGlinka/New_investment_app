from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

API_KEY = os.getenv("API_KEY")

class Cryptocurrency:

    def get_n_top_currency(self, limit_no):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start':'1',
          'limit':limit_no,
          'convert':'USD'
        }
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': API_KEY,
        }

        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            coin_information = []
            for coin in data['data']:
                #print(coin)
                coin_information.append([coin['name'], coin['symbol'], coin['slug'], coin['quote']['USD']['price']])
            return coin_information
            
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
       



# cc = Cryptocurrency()
# cc.get_n_top_currency(10)
# print(cc.get_n_top_currency(10))