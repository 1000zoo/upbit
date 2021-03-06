from decimal import DivisionByZero
import pyupbit as pu
import time
import datetime

import excelog
from ___key___ import Access_Key, Secrete_Key

SEC=1
MIN=60*SEC
HOUR=60*MIN
DAY=24*HOUR

FEE = 0.999
BTC="KRW-BTC"

TARGET = 1.0063
LOSS = 0.9925

COMPARE = 0.9852

ADJ_T = 0.9993
ADJ_L = 1.0013
ADJ_C = 1.0015
data = {
    "time" : [],
    "trade type" : [],
    "trade price" : [],
    "trade volume" : [],
    "target" : [],
    "loss" : [],
    "comp" : []
}
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

    while time.time() - timer < 2*HOUR:
        try:
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
        except KeyboardInterrupt as err:
            print(err)
            break
        
    excelog.excelog(data, title="excelog_test_2")
    print_with_timestemp("end at ")
    print("initial balance: " + str(init_bal))
    print("final balance: " + str(up.get_balance()))

def can_buy(w):
    return w > 9000

def can_sell(v):
    return v > 9000

def hold_range(avg, curr, t, l):
    t = max(t, 1/FEE)
    l = min(l, 1)
    return t*avg < curr or curr < l*avg

def print_with_timestemp(string):
    print(string + str(datetime.datetime.now()))

def buy(up, curr):
    print_time()
    print("buy at " + str(curr))
    d = up.buy_market_order(BTC, up.get_balance()*FEE)
    print("="*15)

def sell(up, avg, curr):
    print_time()
    print("sell at " + str(curr))
    roe = up.get_amount(BTC) * (1.0 - (avg / curr))
    print_rate(avg, curr, roe)
    d = up.sell_market_order("KRW-BTC", up.get_balance("KRW-BTC"))

def update_data(info):
    try:
        data["time"].append(none_check(info["created_at"]))
        data["trade type"].append(none_check(info["side"]))
        data["trade price"].append(none_check(info["price"]))
        data["trade volume"].append(none_check(info["volume"]))
    except KeyError as err:
        print(err)

def none_check(c):
    if c:
        return c
    else:
        return "-"

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
    return time.time() - rtime > 3*MIN

def sell_condition(up):
    return 

if __name__ == '__main__':
    main()