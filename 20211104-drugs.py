import pandas as pd
import numpy as np
from datasets import *

drugs_2018 = pd.read_csv('./data/drugspending2018.csv')
drugs_2019 = pd.read_csv('./data/drugspending2019.csv')
drugs_2020 = pd.read_csv('./data/drugspending2020.csv')

drugs_2018["Year"] = '2018'
drugs_2019["Year"] = '2019'
drugs_2020["Year"] = '2020'

data = drugs_2018.append(drugs_2019).append(drugs_2020)
data.columns = data.columns.str.strip()
data["Rate of \nuse (%)"] = data["Rate of \nuse (%)"].replace('\*\*', np.NaN, regex=True)
data["Rate of \nuse (%)"] = data["Rate of \nuse (%)"].astype('float')

subset = data[data["Age group"] == "Total"]
subset = subset[subset["Sex"] == "Total"]
subset = subset[subset["Jurisdiction"] == "Canada"]

subset = subset[["Year", "Drug class code", "Drug class", "TPS ($ 000)", "Proportion \nof TPS (%)", "Rate of \nuse (%)", "Number of active beneficiaries"]]

by_year = pd.pivot(subset, columns="Year", index=["Drug class code", "Drug class"], values="Rate of \nuse (%)")
by_year["change from 2019"] = by_year["2020"] - by_year["2019"]
by_year["change from 2018"] = by_year["2020"] - by_year["2018"]

print(by_year)
by_year.to_clipboard()