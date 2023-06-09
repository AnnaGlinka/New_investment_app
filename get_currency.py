#https://rapidapi.com/citeamaccount/api/currencyscoop
#stopped working
#https://exchangerate.host/#/#docs

from get_API_data import APIdataGetter


class RealCurrency:

    _APIdataG = APIdataGetter()

    def get_currencies_exchange_rates(self):
        url = "https://api.exchangerate.host/latest"
        #url = "https://api.exchangerate.host/" #wrong url testing
        parameters = {'base': 'USD'}
        exchange_data = self._APIdataG.get_API_data(url, parameters)
        try:
            return exchange_data['rates']  
        except KeyError:
            print(f"Data not available! \nEndpoint: {url}")
#**************************************************************************
    def get_currencies_list(self):
        url = "https://api.exchangerate.host/symbols"
        #url = "https://api.exchangerate.host/sym" #bad endpoint url for testing
        parameters = {'base': 'USD'}
        currency_list = self. _APIdataG.get_API_data(url, parameters)
        try:
            return currency_list['symbols']
        except KeyError:
            print(f"Data not available! \nEndpoint: {url}")
      

#************************************************************************

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

        if exchange_rates == None or curr_data == None:
            return None
        
        combined_data = self.combine_dict(exchange_rates, curr_data)
        sorted_curr_data = dict(sorted(combined_data.items()))

        cleaned_sorted_curr_data = {}

        for key, val in sorted_curr_data.items():
            if type(val[0]) is dict:
                continue
            cleaned_sorted_curr_data.update({key: val})
                
        return  cleaned_sorted_curr_data


# rc = RealCurrency()
# exchage_rates = rc.get_currencies_exchange_rates()
# curr_data = rc.get_currencies_list()
# print(exchage_rates)
# print("")
# print(curr_data)
# print("")
# merged_data = rc.merge_data(exchage_rates, curr_data)
# print(merged_data)
