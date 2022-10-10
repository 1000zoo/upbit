import pyupbit as pu
import time
from util import *
from constant import *
from aiutil import *
import datetime

class myUpbit:
    def __init__(self):
        self.up = login()
        self.balance = 1_000_000
        self.buy_price = 0

    def buy(self, ticker=BTC, amount=10000):
        self.buy_price = pu.get_current_price(BTC)
        print("buy", self.buy_price)

    def sell(self, ticker=BTC, amount=10000):
        curr_price = pu.get_current_price(BTC)
        self.balance = self.balance * (curr_price / self.buy_price)
        print("sell:", curr_price, "/ roe:", curr_price / self.buy_price)

    def print_balance(self):
        time_stamp()
        print(self.balance)

def setup():
    check_path(DPATH)
    check_path(MPATH)

def main():
    up = myUpbit()
    pt = time.time()
    buy = False
    while True:
        pred = predictor()
        roe = pu.get_current_price() / up.buy_price

        if buy and (roe > 1.05 * 0.999 or roe < 0.995 * 0.999):
            up.sell()
            buy = False

        if pred.argmax == 1 and not buy:
            buy = True
            up.buy()
            up.print_balance()
        if pred.argmax == 0 and buy:
            buy = False
            up.sell()
            up.print_balance()

        if _past_time(pt):
            break


def _past_time(_time):
    return time.time() - _time > 5 * 60 * 60

if __name__ == "__main__":
    setup()
    main()