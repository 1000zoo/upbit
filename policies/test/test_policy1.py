import pyupbit as pu

#최대 20봉 안에서 최소값이면 매수
#0.3% 이득 전까지는 매도 X
#잘못된 코드
#최소값 안바뀜

HOUR = 60
DAY = 24
MONTH = 30
XRP = "KRW-XRP"
BTC = "KRW-BTC"
ETH = "KRW-ETH"
ADA = "KRW-ADA"
df = pu.get_ohlcv(XRP, interval="minute1", count=HOUR*DAY*3)

init_money = 1_000_000
current_money = init_money
target_rate = 1.003

count = 0
average_price = 0
buying_money = 0
S = True

for time, low in zip(df.index, df["low"]):
    if count == 0 and S:
        min = low
        count += 1
        continue
    elif count < 20 and S:
        if min > low:
            min = low
        count += 1
        continue
    elif count == 20:
        min = low
        count = 0
    S = False
    k = target_rate * average_price
    if min >= low and current_money != 0:
        buying_money = current_money
        current_money = 0
        average_price = low
        count = 0
        print(str(time) + " : buy at " + str(average_price))
    if low >= k and low - average_price != 0 and buying_money != 0:
        earn_rate = float(low / average_price)
        current_money = earn_rate * buying_money
        buying_money = 0
        print(str(time) + " : sell at " + str(low))
        print("earn rate : " + str(earn_rate))
        print("current money : " + str(current_money))

print(buying_money * pu.get_current_price(XRP) / average_price)