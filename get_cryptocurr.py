
import os
from get_API_data import GetAPIdata

API_KEY = os.getenv("API_KEY")


class Cryptocurrency(GetAPIdata):


    def get_n_top_currency(self, no_of_record:int):
        parameters = {'start': '1', 'limit': no_of_record, 'convert': 'USD'}
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY,
        }
        
        data = super().get_API_data(url, parameters, headers)
        coin_information = []
        for coin in data['data']:
            coin_information.append([coin['name'], coin['symbol'], coin['slug'], coin['quote']['USD']['price']])
          
     
        
        return coin_information
    
      
    
# cc = Cryptocurrency()
# data = cc.get_n_top_currency(10)
# print(data)

