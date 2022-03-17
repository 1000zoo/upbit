from decimal import DivisionByZero
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

TARGET = 1.0043
LOSS = 0.992

COMPARE_A = 0.985
COMPARE_B = 0.9925

def main():
    up = pu.Upbit(Access_Key, Secrete_Key)
    avg_price = 0
    timer = time.time()
    reset_time = timer
    min_price = pu.get_current_price(BTC)
    init_bal = up.get_balance()
    print_with_timestemp("start at ")

    while time.time() - timer < 9*HOUR:
        curr_price = pu.get_current_price(BTC)
        if can_buy(up.get_balance()):
            if buy_condition(reset_time) == "case1":
                min_price = min(min_price, pu.get_current_price(BTC))
                time.sleep(0.5)
                continue
            elif buy_condition(reset_time) == "case2":
                if min_price*COMPARE_A <= pu.get_current_price(BTC):
                    min_price = min(min_price, pu.get_current_price(BTC))
                    time.sleep(0.5)
                    continue
            elif buy_condition(reset_time) == "case3":
                if min_price*COMPARE_B <= pu.get_current_price(BTC):
                    min_price = min(min_price, pu.get_current_price(BTC))
                    time.sleep(0.5)
                    continue
            print_time()
            buy(up)
            avg_price = pu.get_current_price(BTC)
        else:
            curr_price = pu.get_current_price(BTC)
            if TARGET*avg_price < curr_price or \
                curr_price < LOSS*avg_price:
                print_time()
                roe = up.get_amount(BTC) * (1.0 - (avg_price / curr_price))
                sell(up)
                print_rate(avg_price, curr_price, roe)
                reset_time = time.time()
                min_price = pu.get_current_price(BTC)
        time.sleep(0.5)

    print_with_timestemp("end at ")
    print("initial balance: " + str(init_bal))
    print("final balance: " + str(up.get_balance()))

def can_buy(w):
    return w > 5000

def print_with_timestemp(string):
    print(string + str(datetime.datetime.now()))

def buy(up):
    print("buy at " + str(pu.get_current_price(BTC)))
    print_with_timestemp("time : ")
    up.buy_market_order(BTC, up.get_balance()*FEE)
    print("="*15)

def sell(up):
    print("sell")
    print_with_timestemp("time : ")
    up.sell_market_order("KRW-BTC", up.get_balance("KRW-BTC"))

def print_rate(avg, curr, roe):
    try:
        print(avg, curr, curr/avg)
        print("roe : " + str(roe))
        if curr/avg > 1:
            print("gain!!!")
        else:
            print("loss T_T")
    except DivisionByZero as err:
        print(err)
    finally:
        print("="*15)

def print_time():
    print("="*15)
    print(datetime.datetime.now())

def buy_condition(rtime):
    switch = time.time() - rtime
    if switch < 2*MIN:
        return "case1"
    elif switch < 4*MIN:
        return "case2"
    elif switch < 8*MIN:
        return "case3"
    else:
        return "buy"

def sell_condition(up):
    return 

if __name__ == '__main__':
    main()