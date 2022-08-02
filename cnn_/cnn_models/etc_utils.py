import matplotlib.pyplot as plt

def plot_history(history, title="loss", history_type="loss", path_figure=""):
    val = "val_" + history_type

    if len(title.split(".")) == 1:
        title += ".jpg"
    save_path = path_figure + title

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




if __name__ == "__main__":
    pass