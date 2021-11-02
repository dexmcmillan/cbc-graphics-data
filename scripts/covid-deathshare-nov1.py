import pandas as pd
from datawrapper import new_chart
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import *

deaths = pd.read_csv(OWID['covid'])

continents = ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]

groups = deaths[['location', 'continent', 'date', 'new_deaths']]

groups = deaths[deaths["location"].isin(continents)]

pivot = pd.pivot(groups, index="location", columns="date", values="new_deaths").transpose()

for label, content in pivot.items():
    pivot[label] = pivot[label].rolling(7).mean()

print(pivot)
pivot.to_clipboard()

sns.lineplot(data=pivot)
plt.show()