from tensorflow.keras import models, layers, optimizers

def myConv2D(filter, size, input_shape=""):
    if input_shape == "":
        return layers.Conv2D(filter, (size, size), activation="relu", padding="same")
    else:
        return layers.Conv2D(filter, (size, size), activation="relu", padding="same", input_shape=input_shape)

def myMaxPooling(pool_size = 2):
    return layers.MaxPooling2D(pool_size, pool_size)