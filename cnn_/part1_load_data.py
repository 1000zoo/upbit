import pyupbit as pu
from datetime import datetime
import random

"""
target data set:
        * day, 1min~240min
        * 총 8개의 종류로 각 500장씩
        * 총 4000장 (장당 20KB 정도, 총 72MB 정도)
"""

def get_ohlcv(ticker="KRW-BTC", count=31, data_count=500):
    M = "minute"
    interval_list = [0, 1, 5, 10, 15, 30, 60, 240]

    for il in interval_list:
        interval = M + str(il)
        candle = pu.get_ohlcv(ticker, count=count, interval=interval, to=generate_to())
        yield candle


def generate_to():
    year = random.randint(2018,2022)
    if year == 2020:
        Feb = 29
    else:
        Feb = 28
    month = int(random.random()*12) + 1
    day_max = [31,Feb,31,30,31,30,31,31,30,31,30,31]
    day = int(random.random()*day_max[month-1]) + 1
    hour = int(random.random()*24)
    minute = int(random.random()*60)
    tmp = to_format(
        year, month, day, hour, minute
    )
    if int(tmp) > int(now_toformat()):
        generate_to()
    else:
        return tmp
    

def now_toformat():
    now = datetime.now()
    return to_format(
        now.year, now.month, now.day, now.hour, now.minute
    )

def to_format(year, month, day, hour, minute):
    to = ""
    to += my_format(year)
    to += my_format(month)
    to += my_format(day)
    to += my_format(hour)
    to += my_format(minute)
    return to


def my_format(t):
    if t < 10:
        return "0" + str(t)
    else:
        return str(t)

if __name__ == "__main__":
    pass
    