import os

def check_valid_path(root):
    ttv = ["train", "validation", "test"]
    for p in ttv:
        t = os.path.join(root, p)
        try:
            os.listdir(t)
            print(p, "=> valid")
        except:
            os.mkdir(t)
            print("make", p)


def sel(s=""):
    if s == "":
        print("null")
    else:
        print(s)

import my_models as mm

m = mm.model1([128,128,3])
print(type(m))
