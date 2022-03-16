from audioop import avg
import pyupbit as pu
import time
import datetime
from ___key___ import Access_Key, Secrete_Key

SEC=1
MIN=60*SEC
HOUR=60*MIN
DAY=24*HOUR

FEE = 0.9995
BTC="KRW-BTC"

TARGET = 1.007
LOSS = 0.997

def main():
    up = pu.Upbit(Access_Key, Secrete_Key)
    avg_price = 0
    timer = time.time()
    reset_time = time.time()
    min_price = pu.get_current_price(BTC)
    buyT_sellF = True
    init_bal = up.get_balance()
    print("start at" + str(datetime.datetime.now()))

    while time.time() - timer < HOUR:
        curr_price = pu.get_current_price(BTC)
        if buyT_sellF:
            if ask_condition(reset_time) == "wait":
                min_price = min(min_price, pu.get_current_price(BTC))
                time.sleep(0.5)
                continue
            elif ask_condition(reset_time) == "any":
                if min_price <= pu.get_current_price(BTC):
                    time.sleep(0.5)
                    continue
            print_time()
            ask(up)
            print("="*15)
            avg_price = up.get_avg_buy_price(BTC)
            buyT_sellF = False
        else:
            curr_price = pu.get_current_price(BTC)
            if TARGET*avg_price < curr_price or \
                curr_price < LOSS*avg_price:
                print(avg_price, curr_price)
                print(TARGET*avg_price, LOSS*avg_price, curr_price)
                print(curr_price / avg_price)
                print_time()
                bid(up)
                print("="*15)
                buyT_sellF = True
                reset_time = time.time()
                min_price = pu.get_current_price(BTC)
        time.sleep(0.5)

    print("initial balance: " + str(init_bal))
    print("final balance: " + str(up.get_balance()))

def ask(up):
    print(up.buy_market_order(BTC, up.get_balance()*FEE))

def bid(up):
    print(up.sell_market_order("KRW-BTC", up.get_balance("KRW-BTC")))

def print_time():
    print("="*15)
    print(time.time())

def ask_condition(rtime):
    switch = time.time() - rtime
    if switch < 1/6*MIN:
        return "wait"
    elif switch > 0.5*MIN:
        return "ask"
    else:
        return "any"

def bid_condition(up):
    return 

if __name__ == '__main__':
    main()