from get_cryptocurr import Cryptocurrency
from get_currency import RealCurrency
from get_eu_VAT_rates import EuVATRates

#pytest -v -s
#pytest -v -s test_api.py::test_can_call_counties_endpoint
#pytest -v -s test_api.py::test_can_call_covid_per_country_endpoint
#pytest -v -s test_api.py::test_get_country_code


def test_get_n_top_currency():
    cc = Cryptocurrency()
    assert str(type(cc.get_n_top_currency(10))) == "<class 'list'>"

rc = RealCurrency()
def test_get_currencies_exchange_rates():
    assert str(type(rc.get_currencies_exchange_rates())) == "<class 'dict'>"

def test_get_currencies_list():
    assert str(type(rc.get_currencies_list())) == "<class 'dict'>"


def test_merge_data():
    with open('add_files_for_testing/currency_list_for_testing.txt') as list:
        currency = list.readlines()
        currency_list = eval(currency[0]) 

    with open('add_files_for_testing/exchange_rates_for_testing.txt') as exchange:
        exchange = exchange.readlines()
        exchange_rates = eval(exchange[0])

    with open('add_files_for_testing/merged_data_for_testing.txt') as merged:
        merged = merged.readlines()
        merged_currency = eval(merged[0])
    
    assert rc.merge_data(exchange_rates, currency_list) == merged_currency

def test_get_vat_retes():
    eu_vr = EuVATRates()
    assert str(type(eu_vr.get_vat_retes())) == "<class 'dict'>"
  
    
    