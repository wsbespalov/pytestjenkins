from flask import Flask
from flask import request
import json

app = Flask(__name__)


class Wallet:

    def __init__(self, value=0):
        self.__amount = float(value)

    def amount(self):
        return float(self.__amount)

    def debet(self, value):
        self.__amount = self.__amount - value

    def credit(self, value):
        self.__amount = self.__amount + value

wallet = Wallet(0)

@app.route('/')
def amount():
    return json.dumps({'amount': wallet.amount()})

@app.route('/debet')
def debet(self):
    wallet.debet(float(request.args.get('value')))
    return wallet.amount()

@app.route('/credit')
def credit():
    wallet.credit(float(request.args.get('value')))
    return wallet.amount()


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)