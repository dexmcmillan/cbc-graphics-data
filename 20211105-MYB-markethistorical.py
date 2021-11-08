import pandas as pd
import numpy as np
from datasets import *

data = pd.read_csv('./data/historical_stocks.csv')
tse = pd.read_csv('./data/gsptse.csv')

tse.columns = tse.columns.str.strip()
tse = tse[["Date", "Close"]]
tse.columns = ["date", "value"]
tse["market"] = 'GSPTSE'

data = data[data["date"] >= '2016-11-05']
data = data.dropna()

data = data.append(tse)

pivot = pd.pivot(data, columns="market", index="date", values="value")

for label, content in pivot.items():
    pivot[label] = pivot[label].pct_change()

print(pivot)
pivot.to_clipboard()