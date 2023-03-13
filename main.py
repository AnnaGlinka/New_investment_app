from flask import Flask, render_template
from get_cryptocurr import Cryptocurrency

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():

    cc = Cryptocurrency()
    currency_data = cc.get_n_top_currency(10)
    return render_template('index.html', currency_data=currency_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
