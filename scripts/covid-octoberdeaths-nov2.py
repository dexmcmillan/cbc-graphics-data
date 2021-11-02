import pandas as pd
from datawrapper import new_chart
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *
import calendar

deaths = pd.read_csv(COVID['canada'])

deaths = deaths[['prname', 'date', 'numdeathstoday']]
deaths["date"] = pd.to_datetime(deaths["date"])

deaths = deaths[pd.DatetimeIndex(deaths['date']).year >= 2021]
deaths = deaths[~deaths['prname'].isin(["Canada", "Repatriated travellers"])]

group = deaths.groupby(['prname', pd.DatetimeIndex(deaths['date']).month]).sum()
group = group.reset_index()
group['date'] = group["date"].apply(lambda x: calendar.month_abbr[x])

pivot = pd.pivot(group, index="prname", columns="date", values='numdeathstoday')
print(pivot)
pivot.to_clipboard()

# sns.barplot(data=pivot.transpose())
# plt.show()