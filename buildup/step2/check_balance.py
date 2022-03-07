import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import ___key___ as key
import pyupbit as pu

access_key = key.Access_Key
secrete_key = key.Secrete_Key

upbit = pu.Upbit(access_key, secrete_key)

#원화 잔고
balance = upbit.get_balance()
print("-"*30)
print(balance)
print(type(balance))
print(int(balance))

#{ticker} 매수금액
amount = upbit.get_amount("XRP")
print("-"*30)
print(amount)
print(type(amount))

#평단
avg_price = upbit.get_avg_buy_price("XRP")
print("-"*30)
print(avg_price)

#전체 확인
balances = upbit.get_balances()
print("-"*30)
print(balances)
print(type(balances))
