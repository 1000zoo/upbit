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

e1 = 1353.0
e2 = 1302.6
for p in xrp_60m_candle_df["close"]:
    e1 = mym.ema(e1, p, 9)
    e2 = mym.ema(e2, p, 26)
    print(p, e1, e2, end=" ")
    if(mym.check_cross(e1, e2)):
        print("CROSS!", end="")
    print()