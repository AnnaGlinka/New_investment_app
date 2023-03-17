#https://rapidapi.com/citeamaccount/api/currencyscoop
#stopped working
#https://exchangerate.host/#/#docs


from get_API_data import GetAPIdata


class EuVATRates(GetAPIdata):

    def get_vat_retes(self):
        url = "https://api.exchangerate.host/vat_rates"
        EU_VAT_rates = super().get_API_data(url)
    
        for country, rate in EU_VAT_rates['rates'].items():
            if rate['reduced_rates'] == []:
                rate['reduced_rates'] = 'Not applicable'
            if rate['super_reduced_rates'] == []:
                rate['super_reduced_rates'] = 'Not applicable'
            if rate['parking_rates'] == []:
                rate['parking_rates'] = 'Not applicable'
            
        return EU_VAT_rates['rates']


evr = EuVATRates()
vat = evr.get_vat_retes()
print(vat)
