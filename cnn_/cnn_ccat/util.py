import pyupbit as pu
import datetime
import os
from ___key___ import ACCESS_KEY, SECRET_KEY


def login():
    try:
        return pu.Upbit(ACCESS_KEY, SECRET_KEY)
    except Exception as e:
        print("login error")
    finally:
        print("login succeed")


def time_stamp(s="None"):
    print(datetime.datetime.now(), ":", s)


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
