#https://rapidapi.com/citeamaccount/api/currencyscoop
#stopped working
#https://exchangerate.host/#/#docs
#obsluga bledow, testy, dziedziczenie html


from get_API_data import APIdataGetter


class EuVATRates:

    _APIdataG = APIdataGetter()

    def get_vat_retes(self):
        url = "https://api.exchangerate.host/vat_rates"
        #url = "https://api.exchangerate.host/vat_ra" #error in endpoint
        EU_VAT_rates = self._APIdataG.get_API_data(url)

        try:
            for country, rate in EU_VAT_rates['rates'].items():
                if rate['reduced_rates'] == []:
                    rate['reduced_rates'] = 'Not applicable'
                if rate['super_reduced_rates'] == []:
                    rate['super_reduced_rates'] = 'Not applicable'
                if rate['parking_rates'] == []:
                    rate['parking_rates'] = 'Not applicable'
                
            return EU_VAT_rates['rates']
            
        except TypeError:
            print(f"Data not available! \nEndpoint: {url}")


evr = EuVATRates()
vat = evr.get_vat_retes()
print(vat)
