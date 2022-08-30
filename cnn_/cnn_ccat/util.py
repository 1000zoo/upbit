import pyupbit as pu
import datetime
from ___key___ import Access_Key, Secrete_Key


def login() -> pu.exchange_api.Upbit:
    try:
        return pu.Upbit(Access_Key, Secrete_Key)
    except Exception as e:
        print("login error")
    finally:
        print("login succeed")


def time_stamp(s : str):
    print(datetime.datetime.now(), ":", s)