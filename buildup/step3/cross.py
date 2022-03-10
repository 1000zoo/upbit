from culib import mym
import pyupbit as pu

XRP = "KRW-XRP"
xrp_60m_candle_df = pu.get_ohlcv(XRP, interval="minute1" ,count=144)

e1 = 1353.0
e2 = 1302.6
for p in xrp_60m_candle_df["close"]:
    e1 = mym.ema(e1, p, 9)
    e2 = mym.ema(e2, p, 26)
    print(p, e1, e2, end=" ")
    if(mym.check_cross(e1, e2)):
        print("CROSS!", end="")
    print()