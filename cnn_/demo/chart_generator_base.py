import pyupbit as pu
from datetime import datetime
import random

import mplfinance as mpf
from PIL import Image

import os
"""
target data set:
        * 봉 종류: 1min~60min
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
        - generate_images
"""
## 경로설정
PATH = "/Users/1000zoo/Documents/prog/data_files/ccat_data/"
TEST = PATH + "test/"
VAL = PATH + "val/"
TRAIN = PATH + "train/"
DEC = "decrease/"
INC = "increase/"
SID = "sideways/"

## 퍼센테이지 설정
INCPER = 1.01
DECPER = 0.99

## 봉 수 설정
TCOUNT = 41

## 캔들 pandas data 가져오기
def get_ohlcv(ticker="KRW-BTC", count=TCOUNT):
    M = "minute"
    interval_list = [1, 5, 10, 15, 30, 60]

    while True:
        il = random.choice(interval_list)
        interval = M + str(il)
        candle = pu.get_ohlcv(ticker, count=count, interval=interval, to=generate_to())
        yield candle

## 기준일 랜덤 생성기
def generate_to():
    year = random.randint(2018,2022)
    ## 윤년 처리
    ## 추후 윤년을 일반화하는 코드 및 함수 추가
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
    # 현재보다 높은 시간대가 나오면 무시
    if int(tmp) > int(now_toformat()):
        generate_to()
    else:
        return tmp
    
## 현재 시간을 string 형식으로 반환
def now_toformat():
    now = datetime.now()
    return to_format(
        now.year, now.month, now.day, now.hour, now.minute
    )

## 입력된 시간을 string 형식으로 변환
def to_format(year, month, day, hour, minute):
    to = ""
    to += my_format(year)
    to += my_format(month)
    to += my_format(day)
    to += my_format(hour)
    to += my_format(minute)
    return to


## 한 자리 수를 두 자리 수로 변환
def my_format(t):
    if t < 10:
        return "0" + str(t)
    else:
        return str(t)


## main
def generate_images(count=1000, p=TRAIN, ticker="KRW-BTC"):
    ## 변수 초기화
    dcount = icount = scount = 0
    c = 0
    tp = ""

    ## main loop
    for candle in get_ohlcv(ticker=ticker):
        if dcount >= count and icount >= count and scount >= count:
            break

        ## 차트 불러오기 ()
        colorset = mpf.make_marketcolors(up='r', down='b', volume='blue')
        s = mpf.make_mpf_style(marketcolors=colorset)
        chart = mpf.plot(candle[:TCOUNT - 1], type='candle', volume=True, style=s, savefig="test.jpg")
        chart = mpf.plot(candle[:TCOUNT], type='candle', volume=True, style=s, savefig="full.jpg")

        ## p1: 마지막 가격
        ## p2: 정답의 고가
        ## p3: 정답의 저가
        candle.reset_index(drop=False, inplace=True)
        p1 = candle.loc[TCOUNT-2]["close"]
        p2 = candle.loc[TCOUNT-1]["high"]
        p3 = candle.loc[TCOUNT-1]["low"]
        moveto = p

        if p1 * INCPER < p2:
            ## 원하는 데이터 수를 채웠으면 스킵
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
        
        ## 학습용 차트와 확인용 차트 저장
        area = (165, 70, 710, 480)
        img = Image.open("test.jpg")
        crop_img = img.crop(area)
        crop_img.save("crop_test.jpg")

        fig = "./crop_test.jpg"
        newname = str(c) + ".jpg"
        os.replace(fig, moveto + newname)

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