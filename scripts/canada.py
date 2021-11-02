import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

canada = pd.read_csv(COVID['canada'])

canada = canada[["prname", "date", "rateactive"]]

canada["date"] = pd.to_datetime(canada["date"])

latest = canada.groupby("prname").apply(lambda grp: grp.nlargest(60, "date"))

latest = latest[["date", "rateactive"]].reset_index()

pivot = pd.pivot_table(latest, columns="prname", index="date", values="rateactive")

pivot.to_clipboard()
print(pivot)

grid = sns.FacetGrid(data=latest, col="prname", col_wrap=3)
grid.map(sns.lineplot, "date", "rateactive", color="#C42127").set_titles(col_template="{col_name}", row_template="{row_name}")
grid.set_axis_labels("Date", "Rate")
# grid.set(xticks=["2021-10-13", "2021-10-16", "2021-10-19"])
# grid.set_xticklabels(["Oct. 13/21", "Oct. 16/21", "Oct. 19/21"])

for axis in grid.axes.flat:
    axis.tick_params(labelbottom=True)
    axis.tick_params(labelleft=True)



plt.savefig("./charts/covid_cases_by_province_facet.svg", format="svg")
plt.show()
