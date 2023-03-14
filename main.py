from flask import Flask, render_template
from get_cryptocurr import Cryptocurrency
from get_currency import RealCurrency

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    """
    get cryptocurrency part
    """
    cc = Cryptocurrency()
    crypto_data = cc.get_n_top_currency(20)
    currency_symbol = "$"
    """
    get currency exchange rates part
    """

    rc = RealCurrency()
    exchage_rates = rc.get_currencies_exchange_rates()
    curr_data = rc.get_currencies_list()
    currency_data = rc.merge_data(exchage_rates, curr_data)



    
    return render_template('index.html', crypto_data=crypto_data, currency_symbol=currency_symbol, currency_data=currency_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
