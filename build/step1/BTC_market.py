import pyupbit as pu

btc_xrp = pu.get_current_price(["BTC-XRP"])
krw_xrp = pu.get_current_price(["KRW-XRP"])
krw_btc = pu.get_current_price(["KRW-BTC"])
print(btc_xrp, krw_xrp)
print(round(btc_xrp * krw_btc), krw_xrp)