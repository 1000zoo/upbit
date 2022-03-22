import pandas as pd
import datetime as datetime

def excelog(
    data=[],
    labels=[],
    title=datetime.datetime.now(),
    path=""
    ):
    if not data:
        return
    elif labels and type(data) == type([]):
        ex_data = data
        data = {}
        for i, j in zip(labels, ex_data):
            data[i] = j
    if type(title) == type(datetime.datetime.now()):
        title = datetime_to_title(title)
    if path: 
        if path[-1] != "/":
            path += "/"
    path = path + title + ".xlsx"
    print(path)
    df = pd.DataFrame(data)
    df.to_excel(path, index=False)

def datetime_to_title(t):
    if type(t) != type(datetime.datetime.now()):
        return "fail"
    result = "exelog "
    result += str(t.date())
    result += " "
    result += str(t.hour)
    result += "."
    result += str(t.minute)
    result += "."
    result += str(t.second)
    return result
