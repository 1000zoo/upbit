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


def bb(s):
    print(3*s//5, 1*s//5, 1*s//5)



def combined(*args):
    for a in args:
        print(a)

combined(1,2,3,4,5)
