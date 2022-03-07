import os
import sys
from telnetlib import SE
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ___key___ import Access_Key, Secrete_Key
import pyupbit as pu

mu = pu.Upbit(Access_Key, Secrete_Key)
xrp = pu.get_current_price("KRW-XRP")
tprice = 100000
samount = tprice / xrp
rec = mu.sell_limit_order("KRW-XRP", xrp, samount)
print(rec)