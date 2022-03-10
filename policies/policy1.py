from culib import mym
import pyupbit as pu

XRP = "KRW-XRP"
df = pu.get_ohlcv(XRP, interval="minute1", count=10080)

init_money = 1_000_000
current_money = init_money
target_rate = 1.003

fprice = 0
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