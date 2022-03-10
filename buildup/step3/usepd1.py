import pyupbit as pu

M1 = "minute1"
XRP = "KRW-XRP"

xrp_60m_candle_df = pu.get_ohlcv(XRP, interval=M1, count=144)
print((xrp_60m_candle_df))
print(type(xrp_60m_candle_df))
print(str(xrp_60m_candle_df))

print(xrp_60m_candle_df["open"][40])