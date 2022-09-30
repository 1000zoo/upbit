import data_utils as du
import my_models as mm
import etc_utils as eu
import model_utils as mu
import os

import time

#C:\Users\cjswl\python-data\ccat-data\train
DATA_DIR = "C:/Users/cjswl/python-data/ccat-data/"
# DATA_DIR = "/Users/1000zoo/Documents/prog/data_files/dogs_and_cats"
EPOCH = 100
INPUT_SHAPE = (128,128,3)
"""
https://github.com/1000zoo/upbit
"""

# def main():
#     train_data = du.load(DATA_DIR, 0)
#     val_data = du.load(DATA_DIR, 1)
#     test_data = du.load(DATA_DIR, 2)

#     st = time.time()
    
#     model = mm.model1(INPUT_SHAPE)

#     history = model.fit(train_data, epochs=EPOCH, validation_data=val_data)

#     eu.dircheck("model")
#     model_path = os.path.join("model", "model.h5")
#     model.save(model_path)

#     eu.plot_history(history)
#     eu.plot_history(history, "acc", "accuracy")
#     test_loss, test_acc = model.evaluate(test_data)
#     print("test_loss", test_loss)
#     print("test_acc", test_acc)
#     print(time.time() - st)

# def twostep():
#     train_data = du.load(DATA_DIR, 0)
#     val_data = du.load(DATA_DIR, 1)
#     test_data = du.load(DATA_DIR, 2)

#     model = mm.model2(INPUT_SHAPE)
#     pretrain_history = model.fit(
#         train_data, epochs = EPOCH, validation_data = val_data
#     )
#     eu.modeldir()
#     model.save(os.path.join("model", "model2_pretrain.h5"))
#     eu.plot_history(pretrain_history, title="model2_pretrain_loss", history_type="loss")
#     eu.plot_history(pretrain_history, title="model2_pretrain_acc", history_type="accuracy")

#     test_loss, test_acc = model.evaluate(test_data)
#     print("test_loss", test_loss)
#     print("test_acc", test_acc)
    
class Train():
    def __init__(self):
        self.train_data = du.load(DATA_DIR, 0)
        self.val_data = du.load(DATA_DIR, 1)
        self.test_data = du.load(DATA_DIR, 2)

        self.model = mm.model2(INPUT_SHAPE)

    def train(self, model_name, train_type):            
        self.model.summary()

        history = self.model.fit(
            self.train_data, epochs = EPOCH, validation_data = self.val_data
        )
        eu.modeldir()

        title = eu.string_combined(model_name, "_", train_type)
        self.title = eu.string_combined(title, ".h5")

        self.model.save(os.path.join("model", self.title))

        test_loss, test_acc = self.model.evaluate(self.test_data)
        print("test_loss", test_loss)
        print("test_acc", test_acc)

        eu.myPlot(history, title)

    def finetuning(self, model_name):
        self.model = mu.load_model(os.path.join("model", self.title))
    
        conv_base = self.model.layers[0]
        for layer in conv_base.layers:
            if layer.name.startswith("block5"):
                layer.trainable = True
        self.train(model_name, "finetuning")

def main():
    train = Train()
    train.train("model2", "pretrain")
    train.finetuning("model2")

if __name__ == "__main__":
    main()