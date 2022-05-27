import pyupbit as pu
from datetime import datetime
import random

import mplfinance as mpf
from PIL import Image

import os
import copy
"""
target data set:
        * day, 1min~240min
        * 총 8개의 종류로 각 500장씩
        * 총 4000장 (장당 20KB 정도, 총 72MB 정도)

function:
    * for load candle;
        - get_ohlcv
        - generate_to
        - now_toformat
        - to_formate
        - my_format
    
    * for generate & crop & classify;



"""
PATH = "/Users/1000zoo/Documents/prog/data_files/ccat_data/"
TEST = PATH + "test/"
VAL = PATH + "val/"
TRAIN = PATH + "train/"
DEC = "decrease/"
INC = "increase/"
SID = "sideways/"
INCPER = 1.01
DECPER = 0.99
TCOUNT = 41

def get_ohlcv(ticker="KRW-BTC", count=TCOUNT):
    M = "minute"
    interval_list = [1, 5, 10, 15, 30, 60]

    while True:
        il = random.choice(interval_list)
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


def generate_images(count=1000, p=TRAIN, ticker="KRW-BTC"):
    dcount = icount = scount = 0
    c = 0
    tp = ""
    for candle in get_ohlcv(ticker=ticker):
        if dcount >= count and icount >= count and scount >= count:
            break

        colorset = mpf.make_marketcolors(up='r', down='b', volume='blue')
        s = mpf.make_mpf_style(marketcolors=colorset)
        chart = mpf.plot(candle[:TCOUNT - 1], type='candle', volume=True, style=s, savefig="test.jpg")
        chart = mpf.plot(candle[:TCOUNT], type='candle', volume=True, style=s, savefig="full.jpg")

        candle.reset_index(drop=False, inplace=True)
        p1 = candle.loc[TCOUNT-2]["close"]
        p2 = candle.loc[TCOUNT-1]["high"]
        p3 = candle.loc[TCOUNT-1]["low"]
        moveto = p

        if p1 * INCPER < p2:
            if icount < count:
                moveto += INC
                icount += 1
                c = icount
                tp = INC
            else:
                continue
        elif p1 * DECPER > p3:
            if dcount < count:
                moveto += DEC
                dcount += 1
                c = dcount
                tp = DEC
            else:
                continue
        else:
            if scount < count:
                moveto += SID
                scount += 1
                c = scount
                tp = SID
            else:
                continue
        
        area = (165, 70, 710, 480)
        img = Image.open("test.jpg")
        crop_img = img.crop(area)
        crop_img.save("crop_test.jpg")

        fig = "./crop_test.jpg"
        newname = str(c) + ".jpg"
        os.replace(fig, moveto + newname)

        area = (165, 70, 710, 480)
        img = Image.open("full.jpg")
        crop_img = img.crop(area)
        crop_img.save("crop_test_full.jpg")

        fig = "./crop_test_full.jpg"
        newname = str(c) + "full.jpg"
        os.replace(fig, moveto + newname)
        print(tp, c, "full")

if __name__ == "__main__":
    print("generate train data")
    generate_images(5, TRAIN)
    print("generate validation data")
    generate_images(2, VAL)
    print("generate test data")
    generate_images(1, TEST)