import pyupbit as pu
from ___key___ import Access_Key, Secrete_Key
up = pu.Upbit(Access_Key, Secrete_Key)
BTC = "KRW-BTC"
FEE = 0.9995
import time
import datetime
TARGET = 1.003
LOSS = 0.997
up.buy_market_order(BTC, up.get_balance()*FEE)
avg_price = up.get_avg_buy_price(BTC)
while True:
    print("="*15)
    print(datetime.datetime.now(), end=" : ")
    print(pu.get_current_price(BTC))
    print()
    curr_price = pu.get_current_price(BTC)
    print(avg_price, curr_price)
    print(TARGET*avg_price, LOSS*avg_price, curr_price)
    print(curr_price / avg_price)
    if TARGET*avg_price < curr_price or \
        curr_price < LOSS*avg_price:
        up.sell_market_order(BTC, up.get_balance(BTC))
        print("="*15)
        buyT_sellF = True
        reset_time = time.time()
        min_price = pu.get_current_price(BTC)
    time.sleep(0.1)
