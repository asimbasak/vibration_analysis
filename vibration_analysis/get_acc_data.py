import pandas as pd

def get_time_acc(filename,TimeCol, AccCol):
    df = pd.read_csv(filename)

    time = df[TimeCol]
    acc = df[TimeCol]

    return time, acc