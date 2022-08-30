import pyupbit as pu
import time
from util import *
from constant import *
from aiutil import *

class myUpbit():
    def __init__(self):
        self.up = login()

    def buy(self, tiker=BTC, amount=10000):
        up = self.up
        s = (up.buy_market_order(BTC, amount))
        time_stamp(s)
        pass

    def sell(self, tiker=BTC, amount=10000):
        up = self.up
        print(up.sell_market_order(BTC, amount))
        pass

    def print_balance(self):
        up = self.up
        print(up.get_balance())


def main():
    up = myUpbit()
    up.print_balance()
    image_generator()
    print("image load")
    predictor()

if __name__ == "__main__":
    main()