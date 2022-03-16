from ___key___ import Access_Key, Secrete_Key
import pyupbit as pu

up = pu.Upbit(Access_Key, Secrete_Key)

print(up.sell_market_order("KRW-BTC", up.get_balance("KRW-BTC")))