import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

deaths = pd.read_csv(COVID['global_deaths'])
cases = pd.read_csv(COVID['global_cases'])

dates = deaths.columns[4:]

pivot = deaths.melt(id_vars=["Country/Region", "Province/State"], value_vars=dates)

countries = ["Canada", "Russia"]

included_countries = pivot[pivot["Country/Region"].isin(countries)]

grid = sns.barplot(x="Country/Region",
    y='value',
    data=included_countries,
    color="#C42127"
    ).set_title("test CBC graph")

plt.show()
print(pivot)