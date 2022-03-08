###
from math import floor

def vol_to_w(price, vol):
    return floor(price / vol)


def ema(ep, close, r):
    alp = 2 / (r + 1)
    return floor((close * alp) + ep * (1 - alp))