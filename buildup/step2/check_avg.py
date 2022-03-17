import pyupbit as pu
from ___key___ import Access_Key, Secrete_Key
up = pu.Upbit(Access_Key, Secrete_Key)
BTC = "KRW-BTC"

print(up.get_avg_buy_price("KRW-ADA"))