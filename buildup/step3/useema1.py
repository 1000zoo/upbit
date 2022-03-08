import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from culib import mym
from ___key___ import Access_Key, Secrete_Key
import pyupbit as pu
import pandas as pd

mu = pu.Upbit(Access_Key, Secrete_Key)

XRP = "KRW-XRP"
xrp_60m_candle_df = pu.get_ohlcv(XRP, count=144)

e = xrp_60m_candle_df["close"][0]
for p in xrp_60m_candle_df["close"]:
    e = mym.ema(e, p, 9)
    print(e)