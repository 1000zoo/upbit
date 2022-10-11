import pyupbit as pu
import time
from util import *
from constant import *
from aiutil import *
import datetime

"""
지우는 법
WARNING:tensorflow:Error in loading the saved optimizer state. As a result, your model is starting with a freshly initialized optimizer
https://stackoverflow.com/questions/49195189/error-loading-the-saved-optimizer-keras-python-raspberry
"""

class myUpbit:
    def __init__(self):
        self.up = login()
        self.balance = 1_000_000
        self.buy_price = pu.get_current_price(BTC)

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
    st = time.time()
    pt = time.time()
    buy = False
    pred = predictor()
    while True:
        time.sleep(0.5)
        if _past_time(pt, 60):
            pred = predictor()
            pt = time.time()

        if buy:
            roe = pu.get_current_price(BTC) / up.buy_price
            if roe > 1.015 or roe < 0.99:
                up.sell()
                buy = False
            if pred.argmax() == 0:
                buy = False
                up.sell()
                up.print_balance()

        else:
            if pred.argmax() == 1:
                buy = True
                up.buy()
                up.print_balance()

        if _past_time(st, 6 * 60 * 60):
            break


def _past_time(_time, _set_time):
    return time.time() - _time > _set_time

if __name__ == "__main__":
    setup()
    main()

