from pandas import to_datetime
import pyupbit as pu
from datetime import datetime
import random

import mplfinance as mpf
from PIL import Image

import time
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
PATH = "C:/Users/cjswl/python-data/ccat-data/"
TEST = PATH + "test/"
VAL = PATH + "val/"
TRAIN = PATH + "train/"
DEC = "decrease/"
INC = "increase/"
SID = "sideways/"

## 퍼센테이지 설정
INCPER = 1.0019
DECPER = 0.9965

## 봉 수 설정
TCOUNT = 45

## 캔들 pandas data 가져오기
def get_ohlcv(ticker="KRW-BTC", count=TCOUNT):
    M = "minute"
    interval_list = [1, 3, 5, 10, 15, 30, 60]

    while True:
        il = random.choice(interval_list)
        interval = M + str(il)
        to = generate_to()
        candle = pu.get_ohlcv(ticker, count=count, interval=interval, to=to)
        yield to, il, candle

def get_ohlcv_order(ticker="KRW-BTC", count=TCOUNT):
    M = "minute"
    interval_list = [3, 5, 10, 15]

    for il in interval_list:
        interval = M + str(il)
        for to in generate_to_jump(il):
            if int(to) > int(now_toformat()):
                break
            yield to, il, pu.get_ohlcv(ticker, count=count, interval=interval, to=to)

## 기준일 랜덤 생성기
def generate_to():
    year = random.randint(2018,2022)
    ## 윤년 처리
    ## 추후 윤년을 일반화하는 코드 및 함수 추가
    if year == 2020:
        Feb = 29
    else:
        Feb = 28
    day_max = [31,Feb,31,30,31,30,31,31,30,31,30,31]
    month = my_random(12, 1)
    day = my_random(day_max[month-1], 1)
    hour = my_random(24)
    minute = my_random(60)
    tmp = to_format(
        year, month, day, hour, minute
    )
    # 현재보다 높은 시간대가 나오면 무시
    if int(tmp) > int(now_toformat()):
        generate_to()
    else:
        return tmp

## 기준일 순차 생성기
def generate_to_order(il=1):
    years = range(2018, 2023)
    months = range(1,13)
    hours = range(24)
    minutes = range(60//il)
    d28 = [2]
    d30 = [4,6,9,11]
    d31 = [1,3,5,7,8,10,12]

    for year in years:
        for month in months:
            if d28.__contains__(month):
                if year == 2020:
                    days = range(1,30)
                else:
                    days = range(1,29)
            elif d30.__contains__(month):
                days = range(1,31)
            elif d31.__contains__(month):
                days = range(1,32)

            for day in days:
                for hour in hours:
                    for m in minutes:
                        minute = m * il
                        yield to_format(year, month, day, hour, minute)

def generate_to_jump(il = 1):
    years = range(2018, 2023)
    months = range(1,13)
    hours = range(24)
    minutes = range(60//il)
    d28 = [2]
    d30 = [4,6,9,11]
    d31 = [1,3,5,7,8,10,12]

    for year in years:
        for month in months:
            if d28.__contains__(month):
                if year == 2020:
                    days = range(1,30)
                else:
                    days = range(1,29)
            elif d30.__contains__(month):
                days = range(1,31)
            elif d31.__contains__(month):
                days = range(1,32)

            for day in thanos(days):
                for hour in thanos(hours):
                    for m in thanos(minutes):
                        minute = m * il
                        yield to_format(year, month, day, hour, minute)

## 배열 일부 랜덤으로 짜르기
def thanos(arr):
    random.shuffle(arr)
    return arr[:len(arr)//3]

## 월, 일, 시, 분 랜덤 생성
def my_random(x, y=0):
    return int(random.random()*x) + y

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
def generate_images(count=1000, path=TRAIN, ticker="KRW-BTC", shuffle=True, with_sideway=True):
    ## 변수 초기화
    dcount = icount = scount = 0
    c = 0
    tp = ""
    starttime = time.time()

    if shuffle:
        get = get_ohlcv
    else:
        get = get_ohlcv_order

    ## main loop
    for to, il, candle in get(ticker=ticker):
        ## 종료 조건문
        if dcount >= count and icount >= count and scount >= count:
            break
        # if time.time() - starttime > 600:
        #     break

        if il == 1:
            irate = INCPER
            drate = DECPER
        else:
            irate = INCPER * (1 + il * 2 / 10000)
            drate = DECPER * (1 - il * 2 / 10000)

        ## 차트 불러오기 ()
        colorset = mpf.make_marketcolors(up='r', down='b', volume='blue')
        s = mpf.make_mpf_style(marketcolors=colorset)
        mpf.plot(candle[:TCOUNT-5], type='candle', volume=True, style=s, savefig="train.jpg")
        mpf.plot(candle[:], type='candle', volume=True, style=s, savefig="full.jpg")

        ## p1: 마지막 가격
        ## p2: 정답의 고가
        ## p3: 정답의 저가
        ## Heuristic
        candle.reset_index(drop=False, inplace=True)
        p1 = candle.loc[TCOUNT-6]["close"]
        p2 = p3 = 0
        for r in range(1,6):
            p2 += candle.loc[TCOUNT-r]["high"]
            p3 += candle.loc[TCOUNT-r]["low"]

        pinc = p2 / 5
        pdec = p3 / 5
        moveto = path

        ## 최종가격의 INCPER(>1) 배가 pinc보다 낮다면, 상승
        if p1 * irate < pinc:
            ## 원하는 데이터 수를 채웠으면 스킵
            if icount < count:
                moveto += INC
                icount += 1
                c = icount
                tp = INC
            else:
                ## 원하는 데이터 수를 다 채웠어도 일정 확률 이상이면 변경
                if probability(0.09):
                    moveto += INC
                    c = int(random.random() * count) + 1
                    tp = INC
                else:
                    continue
        ## 최종가격의 DECPER(<1) 배가 정답의 평균가보다 높다면, 하락
        elif p1 * drate > pdec:
            if dcount < count:
                moveto += DEC
                dcount += 1
                c = dcount
                tp = DEC
            else:
                if probability(0.09):
                    moveto += DEC
                    c = int(random.random() * count) + 1
                    tp = DEC
                else:
                    continue
        ## 어느쪽에도 해당되지 않는다면 횡보
        else:
            if with_sideway:
                if scount < count:
                    moveto += SID
                    scount += 1
                    c = scount
                    tp = SID
                else:
                    if probability(0.09):
                        moveto += SID
                        c = int(random.random() * count) + 1
                        tp = SID
                    else:
                        continue
            else:
                continue
        
        ## 학습용 차트와 확인용 차트 저장
        area = (165, 70, 710, 480)
        img = Image.open("train.jpg")
        crop_img = img.crop(area)
        crop_img.save("crop_train.jpg")
        fig = "crop_train.jpg"
        newname = str(c) + ".jpg"
        os.replace(fig, moveto + newname)

        ## 원본 차트
        fig = "full.jpg"
        newname = str(c) + "full.jpg"
        os.replace(fig, moveto + newname)
        print(tp, c)

def probability(p):
    return p > random.random()

if __name__ == "__main__":
    generate_images(10000, TRAIN, shuffle=False)
