import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ___key___ import Access_Key, Secrete_Key
import pyupbit as pu
import pandas as pd

mu = pu.Upbit(Access_Key, Secrete_Key)

M1 = "minute1"
M5 = "minute5"
M15 = "minute15"
M30 = "minute30"
M60 = "minute60"
M240 = "minute240"
D = "day"
W = "week"
M = "month"

XRP = "KRW-XRP"

xrp_60m_candle_df = pu.get_ohlcv(XRP, interval=M, count=144)
print((xrp_60m_candle_df))
print(type(xrp_60m_candle_df))
print(str(xrp_60m_candle_df))

print(xrp_60m_candle_df["open"][40])