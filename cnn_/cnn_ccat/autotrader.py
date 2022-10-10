import pyupbit as pu
import time
from util import *
from constant import *
from aiutil import *

class myUpbit:
    def __init__(self):
        self.up = login()

    def buy(self, ticker=BTC, amount=10000):
        up = self.up
        s = (up.buy_market_order(ticker, amount))
        time_stamp(s)
        pass

    def sell(self, ticker=BTC, amount=10000):
        up = self.up
        s = up.sell_market_order(ticker, amount)
        time_stamp(s)
        pass

    def print_balance(self):
        up = self.up
        print(up.get_balance())

def setup():
    check_path(DPATH)
    check_path(MPATH)

def main():
    up = myUpbit()
    up.print_balance()
    image_generator()
    print("image load")
    predictor()

if __name__ == "__main__":
    setup()
    main()