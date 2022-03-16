import pyupbit as pu
from ___key___ import Access_Key, Secrete_Key
FEE = 0.9995
up = pu.Upbit(Access_Key, Secrete_Key)
BTC = "KRW-BTC"
# print(up.buy_market_order("KRW-BTC", up.get_balance()*FEE))

amin = 100_000_000

print(min(amin, pu.get_current_price(BTC)))