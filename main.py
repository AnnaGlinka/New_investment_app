from flask import Flask, render_template, request
from get_cryptocurr import Cryptocurrency
from get_currency import RealCurrency

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    get cryptocurrency part
    """
    cc = Cryptocurrency()
    crypto_data = cc.get_n_top_currency(20)

    """
    get currency exchange rates part
    """

    rc = RealCurrency()
    exchage_rates = rc.get_currencies_exchange_rates()
    curr_data = rc.get_currencies_list()
    currency_data = rc.merge_data(exchage_rates, curr_data)

    """
    get user input
    """
    selected_currency_symbol = request.form.get('currency_symbol')
    currency_exchange_rate = currency_data[selected_currency_symbol][0]

    """
    recalculated cryptocurrency prices
    """
    for crypto in crypto_data:
        crypto[3] = crypto[3] * currency_exchange_rate
    

    return render_template('index.html',
                           crypto_data=crypto_data,
                           currency_symbol=selected_currency_symbol,
                           currency_data=currency_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
