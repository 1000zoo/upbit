import pyupbit as pu

M1 = "minute1"
XRP = "KRW-XRP"

LINE = "-"*15

xrp_candle_df = pu.get_ohlcv(XRP, interval=M1, count=30)
df = xrp_candle_df

print(df)
print(LINE)
print("describe")
print(df.describe()) #df 통계
print(LINE)
print("argmax")
print(df.low.argmax())   #최대,최소 Index num
print(LINE)
print("idxmax")
time = df.low.idxmax()   #최대,최소 Index name?
print(time)
print(time.hour)
print(LINE)
print("quantile")
print(df.quantile(q=0.2))    #0-1 분위수?
print(LINE)
print("mean")
print(df.mean())        #mean
print(LINE)
print("mad")
print(df.mad())         #절대 평균편차?
print(LINE)
print("var")
print(df.var())         #표본분산
print(LINE)