from culib import mym
import pyupbit as pu

XRP = "KRW-XRP"
xrp_60m_candle_df = pu.get_ohlcv(XRP, count=144)

e = xrp_60m_candle_df["close"][0]
for p in xrp_60m_candle_df["close"]:
    e = mym.ema(e, p, 9)
    print(e)