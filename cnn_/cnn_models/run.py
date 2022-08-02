import data_utils as du
import my_models as mm
import etc_utils as eu

import time


DATA_DIR = "/Users/1000zoo/Documents/prog/data_files/ccat_data"
# DATA_DIR = "/Users/1000zoo/Documents/prog/data_files/dogs_and_cats"
EPOCH = 100
INPUT_SHAPE = (128,128,3)


def train():
    pass

def main():
    train_data = du.load(DATA_DIR, 0)
    val_data = du.load(DATA_DIR, 1)
    test_data = du.load(DATA_DIR, 2)

    st = time.time()
    
    model = mm.model1(INPUT_SHAPE)


    history = model.fit(train_data, epochs=EPOCH, validation_data=val_data)

    eu.plot_history(history)
    eu.plot_history(history, "acc", "accuracy")
    test_loss, test_acc = model.evaluate(test_data)
    print("test_loss", test_loss)
    print("test_acc", test_acc)
    print(time.time() - st)





if __name__ == "__main__":
    main()