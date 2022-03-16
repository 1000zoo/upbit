from ___key___ import Access_Key, Secrete_Key
import pyupbit as pu

up = pu.Upbit(Access_Key, Secrete_Key)

my_bal = up.get_balances()
my_vol = up.get_balance("KRW-XRP")

print(my_vol)

# for c in my_bal:
#     if c["currency"] == "XRP":
#         print(c)