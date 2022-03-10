###
from math import floor

def vol_to_w(price, vol):
    return round(price / vol, 1)


def ema(ep, close, r):
    alp = 2 / (r + 1)
    return round((close * alp) + ep * (1 - alp), 1)

def check_cross(ema1, ema2):
    return abs(ema1 - ema2) < 0.3


def buy_point():
    pass