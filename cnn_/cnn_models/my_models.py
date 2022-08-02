"""
모델
"""

from tensorflow.keras import models, layers, optimizers

import model_utils as mu
import matplotlib.pyplot as plt
import os



def model1(input_shape):
    model = models.Sequential()
    model.add(mu.myConv2D(32, 3, input_shape))
    model.add(mu.myMaxPooling())
    model.add(mu.myConv2D(48, 3))
    model.add(mu.myMaxPooling())
    model.add(layers.Dropout(0.5))
    model.add(mu.myConv2D(64, 3))
    model.add(mu.myMaxPooling())
    model.add(mu.myConv2D(96, 3))
    model.add(mu.myMaxPooling())
    model.add(layers.Dropout(0.5))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(3, activation="softmax"))

    model.compile(optimizer=optimizers.Adam(0.0001), loss="categorical_crossentropy", metrics=["accuracy"])

    try:
        model.summary()
    except:
        pass
    
    return model
