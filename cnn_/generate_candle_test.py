"""
Part 1. 과거 데이터 조회
ticker = 종목 이름
count = 불러올 데이터의 수
interval = 몇분 봉, 혹은 몇일 봉을 불러올 것인지
    minute1 / 5 / 10 / 15 ...
to = 언제 데이터를 불러올 것인지
    YYYYMMDDhhmm (ex. 202204212200 이면 2022년 4월 21일 22시 00분 이전의 데이터를 가져옴, 시간은 생략 => 자정기준)
"""
import pyupbit as pu

BTC = "KRW-BTC"
interval = "minute1"
count = 31
to = "202204212200"
candle = pu.get_ohlcv(BTC, count=count, interval=interval, to=to)

"""
Part 2. 과거 데이터를 캔들차트로
1) mplfinance 패키지 이용
2) 추가로 PIL 패키지로 원하는 크기로 캔들차트 이미지 잘라내기
참고 :
1) 
https://wikidocs.net/4766
https://youngwonhan-family.tistory.com/32
https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
2)
https://uipath.tistory.com/94
"""
import mplfinance as mpf

colorset = mpf.make_marketcolors(up='r', down='b', volume='blue')
s = mpf.make_mpf_style(marketcolors=colorset)
chart = mpf.plot(candle[:count - 1], type='candle', volume=True, style=s, savefig="test.jpg")

from PIL import Image
area = (165, 70, 710, 480)
img = Image.open("test.jpg")
crop_img = img.crop(area)
crop_img.save("crop_test.jpg")

"""
Part 3. 캔들차트 분류하기
10 개의 데이터를 불러올 때 (count = 10 일 때),
10 번 째 데이터의 high 가 9 번 째 데이터의 close 보다 
1% 높으면 increase
1% 낮으면 decrease
그 외의 경우 sideways
세 가지 경우로 분류
=> 즉, 매수 시점은 봉이 바뀔 때 (open 일 때)

참고 :
파일 옮기기
https://www.delftstack.com/ko/howto/python/python-move-file/
"""
import os

PATH = "./candle_data/"
DEC = "decrease/"
INC = "increase/"
SID = "sideways/"
INCPER = 1.01
DECPER = 0.99

candle.reset_index(drop=False, inplace=True)
p1 = candle.loc[count-2]["close"]
p2 = candle.loc[count-1]["high"]
fig = "./crop_test.jpg"
newname = "test.jpg"
moveto = PATH

if p1 * INCPER < p2:
    moveto += INC
elif p1 * DECPER > p2:
    moveto += DEC
else:
    moveto += SID

os.replace(fig, moveto + newname)