import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

spending_raw = pd.read_csv('./data/health_spending.csv')


spending1 = spending_raw[spending_raw["Use of Funds"] == "Total"]
spending1 = (spending1[spending1["Sector"].isin(["Public", "Private"])]
                .groupby(["Province", "Year"]).sum().reset_index()
                )
spending1["Current dollars"] = spending1["Current dollars"].astype('int')
spending1["Constant 1997 dollars"] = spending1["Constant 1997 dollars"].astype('int')

spending_2021 = (spending1
            .sort_values('Year', ascending=False)
            .drop_duplicates(subset="Province")
            .set_index('Province')
            )
spending_2021 = spending_2021[["Current dollars per capita", "Constant 1997 dollars per capita"]]


spending_time = spending1[spending1["Province"] == "Canada"].set_index('Year')
spending_time = spending_time[["Current dollars", 'Constant 1997 dollars']]
spending_time["Current dollars"] = spending_time["Current dollars"].astype('int')
spending_time["Constant 1997 dollars"] = spending_time["Constant 1997 dollars"].astype('int')

spending_today = spending_raw[spending_raw["Year"] == 2021]
spending_today = spending_today[spending_today["Sector"].isin(["Public", "Private"])]
spending_today = spending_today.groupby(["Province", "Use of Funds"]).sum().reset_index()
spending_today = spending_today[["Province", 'Use of Funds', 'Current dollars per capita']]
spending_today = spending_today[~spending_today['Use of Funds'].isin(["Total", "Sub-Total"])]

# spending_today_pivot = pd.pivot(spending_today, columns="Use of Funds", index="Province")

print(spending_2021)
spending_2021.to_clipboard()