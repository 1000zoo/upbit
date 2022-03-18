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

COMPARE = 0.985

ADJ_T = 0.999
ADJ_L = 1.001
ADJ_C = 1.005

def main():
    up = pu.Upbit(Access_Key, Secrete_Key)
    timer = time.time()
    reset_time = timer
    min_price = pu.get_current_price(BTC)
    init_bal = up.get_balance()
    avg_price = up.get_avg_buy_price(BTC)
    target = TARGET
    loss = LOSS
    comp = COMPARE
    print_with_timestemp("start at ")

    while time.time() - timer < 0.5*HOUR:
        curr_price = pu.get_current_price(BTC)
        if can_buy(up.get_balance()):
            if past_time(reset_time):
                comp *= ADJ_C
                reset_time = time.time()
            if min_price*comp > curr_price:
                buy(up, curr_price)
                avg_price = pu.get_current_price(BTC)
                print(comp)
                reset_time = time.time()
                comp = COMPARE
            else:
                min_price = min(min_price, curr_price)
        elif can_sell(up.get_amount(BTC)):
            if past_time(reset_time):
                target *= ADJ_T
                loss *= ADJ_L
            if hold_range(avg_price, curr_price, target, loss):
                sell(up, avg_price, curr_price)
                print(target, loss)
                reset_time = time.time()
                min_price = pu.get_current_price(BTC)
                target = TARGET
                loss = LOSS
        else:
            print("no money & coin")
            break
        time.sleep(0.5)

    print_with_timestemp("end at ")
    print("initial balance: " + str(init_bal))
    print("final balance: " + str(up.get_balance()))

def can_buy(w):
    return w > 6000

def can_sell(v):
    return v > 6000

def hold_range(avg, curr, t, l):
    return t*avg < curr or curr < l*avg

def print_with_timestemp(string):
    print(string + str(datetime.datetime.now()))

def buy(up, curr):
    print_time()
    print("buy at " + str(curr))
    up.buy_market_order(BTC, up.get_balance()*FEE)
    print("="*15)

def sell(up, avg, curr):
    print_time()
    print("sell at " + str(curr))
    roe = up.get_amount(BTC) * (1.0 - (avg / curr))
    print_rate(avg, curr, roe)
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

def past_time(rtime):
    return time.time() - rtime > 1*MIN

def sell_condition(up):
    return 

if __name__ == '__main__':
    main()