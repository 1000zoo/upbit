import pyupbit as pu

BTC = "KRW-BTC"
interval = "minute3"
count = 11
to = "202204211123"
candle = pu.get_ohlcv(BTC, count=count, interval=interval, to=to)
print(candle)
candle.reset_index(drop=False, inplace=True)
print(candle.loc[count-3]["high"])