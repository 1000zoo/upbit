import matplotlib.pyplot as plt
import os

def myPlot(history, title):
    loss = string_combined(title, "_loss")
    acc = string_combined(title, "_acc")
    plot_history(history, loss, "loss")
    plot_history(history, acc, "accuracy")

def plot_history(history, title="loss", history_type="loss", path_figure="figure/"):

    dircheck(path_figure)

    val = "val_" + history_type

    if len(title.split(".")) == 1:
        title += ".jpg"
    save_path = os.path.join(path_figure, title)

    if type(history) == dict:
        h = history
    else:
        h = history.history

    plt.plot(h[history_type])
    plt.plot(h[val])
    plt.title(history_type)
    plt.ylabel(history_type)
    plt.xlabel("Epochs")
    plt.legend(["Training", "Validation"], loc=0)
    plt.savefig(save_path)
    plt.clf()

def modeldir():
    dircheck("model")

def dircheck(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def string_combined(*args):
    ret = ""
    for s in args:
        ret += s
    return ret
        
if __name__ == "__main__":
    pass