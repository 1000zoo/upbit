import pyupbit as pu
import mplfinance as mpf
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from util import *
from constant import *


"""
https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment
=> conda 환경에서 pip 설치 에러 관련
"""

IMG = os.path.join(DPATH, "img.jpg")
MODEL = os.path.join("model", "model2.h5")

def fname(interval : str):
    return interval + ".jpg"

def image_generator(ticker="KRW-BTC", count=41, interval="minute3"):
    candle = pu.get_ohlcv(ticker, count=count, interval=interval)
    colorset = mpf.make_marketcolors(up='r', down='b', volume='blue')
    s = mpf.make_mpf_style(marketcolors=colorset)
    file = os.path.join(DPATH, fname(interval))
    mpf.plot(candle, type='candle', volume=True, style=s, savefig=file)
    area = (165, 70, 710, 480)
    img = Image.open(file)
    crop_img = img.crop(area)
    crop_img.save(file)

def img_processing(interval="minute3"):
    image_path = os.path.join(DPATH, fname(interval))
    img = image.load_img(image_path, target_size=(128, 128))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor = preprocess_input(img_tensor)
    return img_tensor

def predictor():
    interval = ["3", "5", "10", "15"]
    sum = np.array([[0.0, 0.0, 0.0]])
    model = load_model(MODEL)
    for i in interval:
        itv = "minute" + i
        image_generator(interval=itv)
        img = img_processing(itv)
        pred = model.predict(img)
        sum += pred
    return sum



