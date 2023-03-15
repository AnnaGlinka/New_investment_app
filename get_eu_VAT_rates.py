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
            return EU_VAT_rates['rates']

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

evr = EuVATRates()
print(evr.get_vat_retes())
