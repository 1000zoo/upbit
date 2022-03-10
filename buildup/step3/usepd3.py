import pyupbit as pu

M1 = "minute1"
XRP = "KRW-XRP"

LINE = "-"*15

df = pu.get_ohlcv(XRP, interval=M1, count=200)
# df = xrp_candle_df.loc["2022-03-10 23:34:00"]
# print(df)

for time, l, value in zip(df.index, df['low'], df['value']):
    print(time, l, value)