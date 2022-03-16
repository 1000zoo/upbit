import pyupbit as pu
from ___key___ import Access_Key, Secrete_Key

up = pu.Upbit(Access_Key, Secrete_Key)

# print(len(up.get_order("KRW-XRP"))==0)
for o in up.get_order("KRW-XRP", state="done"):
    print(o["side"])