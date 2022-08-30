import pyupbit as pu
import mplfinance as mpf
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
import os

"""
https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment
=> conda 환경에서 pip 설치 에러 관련
"""

PATH = "data/"
IMG = os.path.join(PATH, "img.jpg")

def check_path():
    if not os.path.exists(PATH):
        os.mkdir(PATH)

def fname(interval : str) -> str:
    return interval + ".jpg"

def image_generator(ticker="KRW-BTC", count= 41, interval="minute3"):
    check_path()
    candle = pu.get_ohlcv(ticker, count=count, interval=interval, to="202103151500")
    colorset = mpf.make_marketcolors(up='r', down='b', volume='blue')
    s = mpf.make_mpf_style(marketcolors=colorset)
    file = os.path.join(PATH, fname(interval))
    mpf.plot(candle, type='candle', volume=True, style=s, savefig=file)
    area = (165, 70, 710, 480)
    img = Image.open(file)
    crop_img = img.crop(area)
    crop_img.save(file)

def img_processing(interval="minute3"):
    image_path = os.path.join(PATH, fname(interval))
    img = image.load_img(image_path, target_size = (48, 48))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor = preprocess_input(img_tensor)
    return img_tensor

def predictor():
    interval = ["3", "5", "10", "15"]
    sum = np.array([[0.0,0.0,0.0]])
    model = load_model("model/model1.h5")
    for i in interval:
        itv = "minute" + i
        image_generator(interval=itv)
        img = img_processing(itv)
        pred = model.predict(img)
        print(type(pred))
        print(pred)
        sum += pred
    print(sum)
    


