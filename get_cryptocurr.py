import os
from get_API_data import APIdataGetter

API_KEY = os.getenv("API_KEY")


class Cryptocurrency:

    _APIdataG = APIdataGetter()

    def get_n_top_currency(self, no_of_record: int):
        parameters = {'start': '1', 'limit': no_of_record, 'convert': 'USD'}
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': "kkds",
        }

        data = self._APIdataG.get_API_data(url, parameters, headers)

        try:
            coin_information = []
            for coin in data['data']:
                coin_information.append([
                    coin['name'], coin['symbol'], coin['slug'],
                    coin['quote']['USD']['price']
                ])
            return coin_information
        except TypeError:
            print(f"Data not available! \nEndpoint: {url}")
   
        


# cc = Cryptocurrency()
# data = cc.get_n_top_currency(10)
# print(data)
