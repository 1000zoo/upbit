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

TARGET = 1.0033
LOSS = 0.99

COMPARE_A = 0.988
COMPARE_B = 0.995

def main():
    up = pu.Upbit(Access_Key, Secrete_Key)
    avg_price = 0
    buyT_sellF = True
    timer = time.time()
    reset_time = timer
    min_price = pu.get_current_price(BTC)
    init_bal = up.get_balance()
    print_with_timestemp("start at ")

    while time.time() - timer < 8*HOUR:
        curr_price = pu.get_current_price(BTC)
        if buyT_sellF:
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
            buyT_sellF = False
        else:
            curr_price = pu.get_current_price(BTC)
            if TARGET*avg_price < curr_price or \
                curr_price < LOSS*avg_price:
                print_time()
                sell(up)
                print_rate(avg_price, curr_price)
                buyT_sellF = True
                reset_time = time.time()
                min_price = pu.get_current_price(BTC)
        time.sleep(0.5)

    print_with_timestemp("end at ")
    print("initial balance: " + str(init_bal))
    print("final balance: " + str(up.get_balance()))


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

def print_rate(avg, curr):
    try:
        print(avg, curr, curr/avg)
        if curr/avg > 1:
            print("gain!!!")
        else:
            print("loss T_T")
    except DivisionByZero as err:
        print(err)
    finally:
        print("="*15)

def print_time(avg=0, curr=0):
    print("="*15)
    print(datetime.datetime.now())

def buy_condition(rtime):
    switch = time.time() - rtime
    if switch < 1*MIN:
        return "case1"
    elif switch < 7*MIN:
        return "case2"
    elif switch < 20*MIN:
        return "case3"
    else:
        return "buy"

def sell_condition(up):
    return 

if __name__ == '__main__':
    main()