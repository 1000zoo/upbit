from tensorflow.keras import models, layers, optimizers

def myConv2D(filter, size, input_shape=""):
    if input_shape == "":
        return layers.Conv2D(filter, (size, size), activation="relu", padding="same")
    else:
        return layers.Conv2D(filter, (size, size), activation="relu", padding="same", input_shape=input_shape)

def myMaxPooling(pool_size = 2):
    return layers.MaxPooling2D(pool_size, pool_size)

def reluDense(neuron):
    return layers.Dense(neuron, activation = "relu")

def softmaxDense(neuron = 3):
    return layers.Dense(neuron, activation = "softmax")

def myCompile(model):
    model.compile(
            optimizer = optimizers.RMSprop(learning_rate=1e-5),
            loss = "categorical_crossentropy", metrics = ["accuracy"]
    )