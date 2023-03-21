from get_cryptocurr import Cryptocurrency
from get_currency import RealCurrency


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
    