#https://rapidapi.com/citeamaccount/api/currencyscoop
#stopped working
#https://exchangerate.host/#/#docs

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class EuVATRates:

    def get_vat_retes(self):
        url = "https://api.exchangerate.host/vat_rates"
    
        session = Session()

        try:
            response = session.get(url)
            EU_VAT_rates = json.loads(response.text)

            for country, rate in EU_VAT_rates['rates'].items():
                if rate['reduced_rates'] == []:
                    rate['reduced_rates'] = 'Not applicable'
                if rate['super_reduced_rates'] == []:
                    rate['super_reduced_rates'] = 'Not applicable'
                if rate['parking_rates'] == []:
                    rate['parking_rates'] = 'Not applicable'
                    
                print(rate)


            
            return EU_VAT_rates['rates']

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

evr = EuVATRates()
evr.get_vat_retes()
