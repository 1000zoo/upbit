###
from math import floor

def vol_to_w(price, vol):
    return round(price / vol, 1)


def ema(ep, close, r):
    alp = 2 / (r + 1)
    return floor((close * alp) + ep * (1 - alp))

def check_cross(ema1, ema2):
    return ema1 == ema2