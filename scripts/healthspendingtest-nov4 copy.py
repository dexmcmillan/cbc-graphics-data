import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

spending_raw = pd.read_csv('./data/health_spending.csv')


spending_raw = spending_raw[spending_raw["Use of Funds"] == "Total"]
spending_raw = (spending_raw[spending_raw["Sector"].isin(["Public", "Private"])]
                .groupby(["Province", "Year"]).sum().reset_index()
                )
spending_raw["Current dollars"] = spending_raw["Current dollars"].astype('int')
spending_raw["Constant 1997 dollars"] = spending_raw["Constant 1997 dollars"].astype('int')

spending = spending_raw[spending_raw["Year"].isin([2019, 2020, 2021])]
spending = spending[["Year", "Province", "Current dollars per capita"]]

pivot = pd.pivot(spending, columns="Year", index="Province").reset_index()
pivot.columns = ["Province", "2019", "2020", "2021"]
pivot["2019 difference"] = (pivot["2021"] - pivot["2019"])/pivot["2019"]
pivot["2020 difference"] = (pivot["2021"] - pivot["2020"])/pivot["2020"]

print(pivot)
pivot.to_clipboard()