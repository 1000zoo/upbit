import pyupbit as pu

df = pu.get_ohlcv("KRW-BTC", interval="minute30", count=20)
print(df)