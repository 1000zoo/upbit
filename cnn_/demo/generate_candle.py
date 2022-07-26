## import
import os
import pyupbit as pu
import mplfinance as mpf
from PIL import Image

## constants
# path
PATH = "./candle_data/"
DEC = "decrease/"
INC = "increase/"
SID = "sideways/"
JPG = ".jpg"

# for pyupbit
BTC = "KRW-BTC"
INTERVAL = "minute5"
COUNT = 31

# for mplfinance
COLORSET = mpf.make_marketcolors(up='r', down='b', volume='blue')
STYLE = mpf.make_mpf_style(marketcolors=COLORSET)
FIGNAME = "fig" + JPG

# for Image
AREA = (165, 70, 710, 480)

# for classification
INCPER = 1.01
DECPER = 0.99

# etc.
DECCOUNT = 10
INCCOUNT = 10
SIDCOUNT = 10

## main
dcount = icount = scount = 0

while dcount > DECCOUNT and icount > INCCOUNT and scount > SIDCOUNT:
    pass
