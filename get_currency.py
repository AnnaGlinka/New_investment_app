#https://rapidapi.com/citeamaccount/api/currencyscoop
#stopped working
#https://exchangerate.host/#/#docs

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class RealCurrency:

    def get_currencies_exchange_rates(self):
        url = "https://api.exchangerate.host/latest"

        session = Session()

        try:
            response = session.get(url)
            exchange_data = json.loads(response.text)
            #print(exchange_data['rates'])
            return exchange_data['rates']

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def get_currencies_list(self):
        url = "https://api.exchangerate.host/symbols"

        session = Session()
  
        try:
            response = session.get(url)
            currency_list = json.loads(response.text)
            #print(currency_list['symbols'])
            return currency_list['symbols']
           

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def combine_dict(self, d1, d2):
        return {
            k: tuple(d[k] for d in (d1, d2) if k in d)
            for k in set(d1.keys()) and set(d2.keys())
        }

    def merge_data(self, exchange_rates: dict, curr_data: dict) -> dict:
        """
        this function merges dictionaries with available currencies with their 
        exchange rates and returns a dict of currencies with exchange rates
        and names
        """
        combined_data = self.combine_dict(exchange_rates, curr_data)
        sorted_curr_data = dict(sorted(combined_data.items()))
      

        return sorted_curr_data


rc = RealCurrency()
exchage_rates = rc.get_currencies_exchange_rates()
curr_data = rc.get_currencies_list()
#print(exchage_rates)
#print(curr_data)
merged_data = rc.merge_data(exchage_rates, curr_data)
print(merged_data)
